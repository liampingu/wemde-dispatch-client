# coding: utf-8

"""
    WEMDE Dispatch

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from wemde_dispatch_client.models.slack_variable import SlackVariable
from typing import Optional, Set
from typing_extensions import Self

class Constraint(BaseModel):
    """
    Constraint
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="Id of the constraint")
    description: Optional[StrictStr] = Field(default=None, description="Detailed description of the constraint")
    left_hand_side_value: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Resolved value of the LHS of the constraint", alias="leftHandSideValue")
    operator: Optional[StrictStr] = Field(default=None, description="Operator of the constraint")
    constraint_type: Optional[StrictStr] = Field(default=None, description="Constraint Type", alias="constraintType")
    right_hand_side_value: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Resolved value of the RHS of the constraint", alias="rightHandSideValue")
    default_rhs: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Default RHS value of the constraint", alias="defaultRhs")
    binding_constraint_flag: Optional[StrictBool] = Field(default=None, description="Determines if the constraint is binding or not", alias="bindingConstraintFlag")
    near_binding_constraint_flag: Optional[StrictBool] = Field(default=None, description="Indicates if the constraint is within 10% of binding - the resolved LHS value is within 10% of the resolved RHS value.", alias="nearBindingConstraintFlag")
    shadow_price: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Marginal value of the constraint.", alias="shadowPrice")
    is_intervention_event: Optional[StrictBool] = Field(default=None, alias="isInterventionEvent")
    slack_variables: Optional[List[SlackVariable]] = Field(default=None, description="Array of slack variables associated with the constraint", alias="slackVariables")
    __properties: ClassVar[List[str]] = ["id", "description", "leftHandSideValue", "operator", "constraintType", "rightHandSideValue", "defaultRhs", "bindingConstraintFlag", "nearBindingConstraintFlag", "shadowPrice", "isInterventionEvent", "slackVariables"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Constraint from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in slack_variables (list)
        _items = []
        if self.slack_variables:
            for _item in self.slack_variables:
                if _item:
                    _items.append(_item.to_dict())
            _dict['slackVariables'] = _items
        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if left_hand_side_value (nullable) is None
        # and model_fields_set contains the field
        if self.left_hand_side_value is None and "left_hand_side_value" in self.model_fields_set:
            _dict['leftHandSideValue'] = None

        # set to None if operator (nullable) is None
        # and model_fields_set contains the field
        if self.operator is None and "operator" in self.model_fields_set:
            _dict['operator'] = None

        # set to None if constraint_type (nullable) is None
        # and model_fields_set contains the field
        if self.constraint_type is None and "constraint_type" in self.model_fields_set:
            _dict['constraintType'] = None

        # set to None if right_hand_side_value (nullable) is None
        # and model_fields_set contains the field
        if self.right_hand_side_value is None and "right_hand_side_value" in self.model_fields_set:
            _dict['rightHandSideValue'] = None

        # set to None if default_rhs (nullable) is None
        # and model_fields_set contains the field
        if self.default_rhs is None and "default_rhs" in self.model_fields_set:
            _dict['defaultRhs'] = None

        # set to None if binding_constraint_flag (nullable) is None
        # and model_fields_set contains the field
        if self.binding_constraint_flag is None and "binding_constraint_flag" in self.model_fields_set:
            _dict['bindingConstraintFlag'] = None

        # set to None if near_binding_constraint_flag (nullable) is None
        # and model_fields_set contains the field
        if self.near_binding_constraint_flag is None and "near_binding_constraint_flag" in self.model_fields_set:
            _dict['nearBindingConstraintFlag'] = None

        # set to None if shadow_price (nullable) is None
        # and model_fields_set contains the field
        if self.shadow_price is None and "shadow_price" in self.model_fields_set:
            _dict['shadowPrice'] = None

        # set to None if is_intervention_event (nullable) is None
        # and model_fields_set contains the field
        if self.is_intervention_event is None and "is_intervention_event" in self.model_fields_set:
            _dict['isInterventionEvent'] = None

        # set to None if slack_variables (nullable) is None
        # and model_fields_set contains the field
        if self.slack_variables is None and "slack_variables" in self.model_fields_set:
            _dict['slackVariables'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Constraint from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "description": obj.get("description"),
            "leftHandSideValue": obj.get("leftHandSideValue"),
            "operator": obj.get("operator"),
            "constraintType": obj.get("constraintType"),
            "rightHandSideValue": obj.get("rightHandSideValue"),
            "defaultRhs": obj.get("defaultRhs"),
            "bindingConstraintFlag": obj.get("bindingConstraintFlag"),
            "nearBindingConstraintFlag": obj.get("nearBindingConstraintFlag"),
            "shadowPrice": obj.get("shadowPrice"),
            "isInterventionEvent": obj.get("isInterventionEvent"),
            "slackVariables": [SlackVariable.from_dict(_item) for _item in obj["slackVariables"]] if obj.get("slackVariables") is not None else None
        })
        return _obj


