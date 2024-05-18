from functools import partial
from typing import Union

from dash.dependencies import _Wildcard


def form_dependent_id(component: str, aio_id: Union[str, _Wildcard], form_id: Union[str, _Wildcard]) -> dict:
    """A component id to do callbacks at the document level (e.g. edit/delete)."""
    return {"component": component, "aio_id": aio_id, "form_id": form_id}


def field_dependent_id(  # noqa: PLR0913
    component: str,
    aio_id: Union[str, _Wildcard],
    form_id: Union[str, _Wildcard],
    field: Union[str, _Wildcard],
    parent: Union[str, _Wildcard] = "",
    meta: Union[str, _Wildcard] = "",
) -> dict:
    """A component id to do callbacks at the field level (e.g. in the form)."""
    return {
        "component": component,
        "aio_id": aio_id,
        "form_id": form_id,
        "field": field,
        "parent": parent,
        "meta": meta,
    }


value_field = partial(field_dependent_id, "_pydf-value-field")
checked_field = partial(field_dependent_id, "_pydf-checked-field")