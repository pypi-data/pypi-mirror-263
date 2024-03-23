"""Requests module.

Contains structs to build a :class:`DataRequest` instance: an object to describe
the parameters needed for the query using only entity names and relationships.
"""

import hashlib
from dataclasses import dataclass, field
from functools import cached_property
from itertools import chain
from typing import Mapping, Optional, Set, Tuple, Union

from typing_extensions import Literal, Protocol, TypedDict

from tesseract_olap.common import Array

from .models import (
    CutIntent,
    DoubleFilterCondition,
    FilterIntent,
    PaginationIntent,
    SingleFilterCondition,
    SortingIntent,
    TimeRestriction,
)

AnyRequest = Union["DataRequest", "MembersRequest"]


class RequestWithRoles(Protocol):
    """Defines an interface of commons between DataRequest and MembersRequest."""

    cube: str
    roles: Set[str]


class DataRequestOptionalParams(TypedDict, total=False):
    """Defines the optional parameters in the DataRequestParams interface.

    Is a separate class is due to the implementation of the
    [Totality](https://www.python.org/dev/peps/pep-0589/#totality) in the
    :class:`TypedDict` class.

    This will give a better hint to the type checker when the user makes use of
    this interface.
    """

    captions: Array[str]
    cuts_exclude: Mapping[str, Array[str]]
    cuts_include: Mapping[str, Array[str]]
    filters: Mapping[str, Union[SingleFilterCondition, DoubleFilterCondition]]
    locale: str
    pagination: Union[str, Tuple[int, int]]
    parents: Union[bool, Array[str]]
    properties: Array[str]
    ranking: Union[bool, Mapping[str, Literal["asc", "desc"]]]
    roles: Array[str]
    sorting: Tuple[str, Literal["asc", "desc"]]
    time: str


class DataRequestParams(DataRequestOptionalParams, total=True):
    """DataRequestParams interface.

    Determines the expected params in a :class:`dict`, to use when creating a
    new :class:`DataRequest` object via the :func:`DataRequest.new` class method.
    """

    drilldowns: Array[str]
    measures: Array[str]


@dataclass(eq=False, order=False)
class DataRequest:
    """Represents the intent for a Data Query made by the user.

    All its properties are defined by strings of the names of the components
    from the schema.
    None of these parameters are verified during construction, so it's possible
    for the query to be invalid; a subclass of :class:`backend.exceptions.BackendError`
    will be raised in that case.
    The only purpose of this structure is containing and passing over the query
    intent to the internals.

    During a request, a :class:`Query` instance is constructed with objects from
    a schema, using parameters from this instance.
    """

    cube: str
    drilldowns: Set[str]
    measures: Set[str]
    captions: Set[str] = field(default_factory=set)
    cuts: Mapping[str, "CutIntent"] = field(default_factory=dict)
    filters: Mapping[str, "FilterIntent"] = field(default_factory=dict)
    locale: Optional[str] = None
    options: Mapping[str, bool] = field(default_factory=dict)
    pagination: "PaginationIntent" = field(default_factory=PaginationIntent)
    parents: Union[bool, Set[str]] = False
    properties: Set[str] = field(default_factory=set)
    ranking: Union[bool, Mapping[str, Literal["asc", "desc"]]] = False
    roles: Set[str] = field(default_factory=set)
    sorting: Optional["SortingIntent"] = None
    time_restriction: Optional["TimeRestriction"] = None

    def __eq__(self, __value: object) -> bool:
        return isinstance(__value, DataRequest) and hash(self) == hash(__value)

    def __hash__(self):
        return hash((*sorted(self.roles), self.request_id))

    @classmethod
    def new(cls, cube: str, request: DataRequestParams):
        """Creates a new :class:`DataRequest` instance from a set of parameters
        defined in a dict.

        This should be the preferred method by final users, as it doesn't
        require the use of internal dataclasses and the setup of internal
        structures and unique conditions.
        """

        cuts_include = request.get("cuts_include", {})
        cuts_exclude = request.get("cuts_exclude", {})
        filters = request.get("filters", {})
        roles = request.get("roles", [])

        kwargs = {
            "locale": request.get("locale"),
            "cuts": {
                item: CutIntent.new(
                    level=item,
                    incl=cuts_include.get(item, []),
                    excl=cuts_exclude.get(item, []),
                )
                for item in set(chain(cuts_include.keys(), cuts_exclude.keys()))
            },
            "filters": {
                item: FilterIntent.new(field=item, condition=condition)
                for item, condition in filters.items()
            },
            "captions": set(request.get("captions", [])),
            "properties": set(request.get("properties", [])),
            "options": {},
            "ranking": request.get("ranking", False),
            "roles": set(roles) if isinstance(roles, (list, tuple)) else roles,
        }

        item = request.get("pagination", (0, 0))
        if isinstance(item, str):
            kwargs["pagination"] = PaginationIntent.from_str(item)
        elif isinstance(item, (list, tuple)):
            kwargs["pagination"] = PaginationIntent(*item)

        item = request.get("parents", False)
        if isinstance(item, (set, bool)):
            kwargs["parents"] = item
        elif isinstance(item, (list, tuple)):
            kwargs["parents"] = set(item)
        elif isinstance(item, str):
            kwargs["parents"] = {item}

        item = request.get("sorting")
        if isinstance(item, str):
            kwargs["sorting"] = SortingIntent.from_str(item)
        elif isinstance(item, (list, tuple)):
            kwargs["sorting"] = SortingIntent.new(*item)

        item = request.get("time")
        if isinstance(item, str):
            kwargs["time_restriction"] = TimeRestriction.from_str(item)

        return cls(
            cube=cube,
            drilldowns=set(request["drilldowns"]),
            measures=set(request["measures"]),
            **kwargs,
        )

    @cached_property
    def request_id(self):
        """Generates a hash to differentiate the parameters that influence the resulting data.

        This hash can be used to compare requests, and as cache key for the resulting data.
        It doesn't consider roles on purpose, as the roles define the access to the dataset
        instead of its contents. This also means a comparison operation between requests must
        compare roles separetely.
        """
        measures = (
            stringify_filter(name, name in self.measures, self.filters.get(name))
            for name in sorted(self.measures.union(self.filters.keys()))
        )
        drilldowns = (
            stringify_cut(name, name in self.drilldowns, self.cuts.get(name))
            for name in sorted(self.drilldowns.union(self.cuts.keys()))
        )
        parents = (
            f"Parents({self.parents})"
            if isinstance(self.parents, bool)
            else f"Parents({str(sorted(self.parents))[1:-1]})"
        )
        ranking = (
            ", ".join(sorted(f"{key}={value}" for key, value in self.ranking.items()))
            if isinstance(self.ranking, Mapping)
            else self.ranking
        )
        sorting = (
            str(self.sorting).replace("Intent", "") if self.sorting else "Sorting(None)"
        )
        time = (
            str(self.time_restriction).replace("Restriction", "")
            if self.time_restriction
            else "Time(None)"
        )
        params = [
            f"Cube: {self.cube}",
            *measures,
            *drilldowns,
            f"Captions: {sorted(self.captions)}",
            f"Properties: {sorted(self.properties)}",
            f"Locale: {self.locale}",
            f"Pagination: {tuple(self.pagination)}",
            parents,
            f"Ranking({ranking})",
            sorting,
            time,
            # *(f"{key.capitalize()}: {value}" for key, value in self.options.items()),
        ]
        return hashlib.md5("\n".join(params).encode("utf-8")).hexdigest()


def stringify_cut(name: str, is_drilldown: bool, item: Optional[CutIntent]):
    string = f"Level '{name}': {is_drilldown}"
    if item is not None:
        if len(item.include_members) > 0:
            string += f"\n  with {sorted(item.include_members)}"
        if len(item.exclude_members) > 0:
            string += f"\n  without {sorted(item.include_members)}"
    return string


def stringify_filter(name: str, is_measure: bool, item: Optional[FilterIntent]):
    string = f"Measure '{name}': {is_measure}"
    if item is not None:
        string += f"\n  where {item.condition[0][0]} {item.condition[0][1]}"
        if len(item.condition) == 3:
            string += "\n  {joint:>5} {cond[0]} {cond[1]}".format(
                joint=item.condition[1], cond=item.condition[2]
            )
    return string


class MembersRequestOptionalParams(TypedDict, total=False):
    """Defines the optional parameters in the MembersRequestParams interface.

    Is a separate class is due to the implementation of the
    [Totality](https://www.python.org/dev/peps/pep-0589/#totality) in the
    :class:`TypedDict` class.

    This will give a better hint to the type checker when the user makes use of
    this interface.
    """

    children: bool
    locale: str
    pagination: Tuple[int, int]
    parents: bool
    roles: Array[str]
    search: str


class MembersRequestParams(MembersRequestOptionalParams, total=True):
    """MembersRequestParams interface.

    Determines the expected params in a :class:`dict`, to use when creating a
    new :class:`MembersRequest` object via the :func:`MembersRequest.new` class
    method.
    """

    level: str


@dataclass(eq=False, order=False)
class MembersRequest:
    """Represents the intent for a Level Metadata Query made by the user.

    Parameters are constructed with primitives that describe the entities being
    requested.

    It is suggested to use the :func:`MembersRequest.new` method to create a new
    instance of this class, instead of calling a new instance directly.
    """

    cube: str
    level: str
    locale: Optional[str] = None
    options: Mapping[str, bool] = field(default_factory=dict)
    pagination: "PaginationIntent" = field(default_factory=PaginationIntent)
    roles: Set[str] = field(default_factory=set)
    search: Optional[str] = None

    @classmethod
    def new(cls, cube: str, request: MembersRequestParams):
        """Creates a new :class:`MembersRequest` instance from a set of parameters
        defined in a dict.

        This should be the preferred method by final users, as it doesn't
        require the use of internal dataclasses and the setup of internal
        structures and unique conditions.
        """

        item = request.get("pagination", (0, 0))
        pagination = PaginationIntent(*item)

        item = request.get("roles", [])
        roles = set(item) if isinstance(item, (list, tuple)) else item

        return cls(
            cube=cube,
            level=request["level"],
            locale=request.get("locale"),
            options={
                "parents": request.get("parents", False),
                "children": request.get("children", False),
            },
            pagination=pagination,
            roles=roles,
            search=request.get("search"),
        )
