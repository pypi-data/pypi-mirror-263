# SPDX-FileCopyrightText: 2023 German Aerospace Center <fame@dlr.de>
#
# SPDX-License-Identifier: Apache-2.0

from typing import Dict, List

import pytest
from fameio.source.scenario import Attribute, Contract, Agent
from fameio.source.schema import AttributeSpecs, Schema
from fameio.source.validator import AttributeType, SchemaValidator, ValidationException

from .utils import assert_exception_contains, new_agent, new_attribute, new_schema


def new_specs(definitions: List[dict]) -> Dict[str, AttributeSpecs]:
    """Converts list of AttributeSpec definitions to dictionary of name -> AttributeSpecs"""
    specs = {}
    for definition in definitions:
        for name, content in definition.items():
            specs[name] = AttributeSpecs(name, content)
    return specs


def new_contract(sender: int, receiver: int, product: str) -> Contract:
    """Creates a new Contract with given ids for `sender` and `receiver` plus specified `product`"""
    return Contract.from_dict(
        {
            "SenderId": sender,
            "ReceiverId": receiver,
            "ProductName": product,
            "FirstDeliveryTime": 0,
            "DeliveryIntervalInSteps": 1,
        }
    )


class Test:
    def test_get_agent(self):
        schema = Schema.from_dict(new_schema([new_agent("MyAgent", [], [])]))
        assert SchemaValidator._get_agent(schema, "MyAgent")

    def test_get_agent_missing(self):
        schema = Schema.from_dict(new_schema([new_agent("MyAgent", [], [])]))
        with pytest.raises(ValidationException) as e_info:
            SchemaValidator._get_agent(schema, "MissingAgent")
        assert_exception_contains(SchemaValidator._AGENT_TYPE_UNKNOWN, e_info)

    def test_ensure_mandatory_is_present_no_nested(self):
        attributes = {
            "AttribA": Attribute("AttribA", 55),
            "AttribB": Attribute("AttribB", 44),
        }
        specifications = new_specs(
            [
                new_attribute("AttribA", "double", True, False, []),
                new_attribute("AttribB", "double", False, False, []),
            ]
        )
        SchemaValidator._ensure_mandatory_present(attributes, specifications)

    def test_ensure_mandatory_is_present_default_provided(self):
        attributes = {"AttribA": Attribute("AttribA", 55)}
        specifications = new_specs(
            [
                new_attribute("AttribA", "double", False, False, []),
                new_attribute("AttribB", "double", True, False, None, None, "33.3"),
            ]
        )
        SchemaValidator._ensure_mandatory_present(attributes, specifications)

    def test_ensure_mandatory_is_present_nested(self):
        attributes = {"AttribA": Attribute("AttribA", {"AttribB": 44})}
        specifications = new_specs(
            [
                new_attribute(
                    "AttribA",
                    "block",
                    True,
                    False,
                    [new_attribute("AttribB", "double", True, False, [])],
                )
            ]
        )
        SchemaValidator._ensure_mandatory_present(attributes, specifications)

    def test_ensure_mandatory_is_present_top_level_missing_mandatory(self):
        attributes = {"AttribA": Attribute("AttribA", 55)}
        specifications = new_specs(
            [
                new_attribute("AttribA", "double", True, False, []),
                new_attribute("AttribB", "double", True, False, []),
            ]
        )
        with pytest.raises(ValidationException) as e_info:
            SchemaValidator._ensure_mandatory_present(attributes, specifications)
        assert_exception_contains(SchemaValidator._ATTRIBUTE_MISSING, e_info)

    def test_ensure_mandatory_is_present_top_level_missing_optional(self):
        attributes = {"AttribA": Attribute("AttribA", 55)}
        specifications = new_specs(
            [
                new_attribute("AttribA", "double", True, False, []),
                new_attribute("AttribB", "double", False, False, []),
            ]
        )
        SchemaValidator._ensure_mandatory_present(attributes, specifications)

    def test_ensure_mandatory_is_present_nested_missing_mandatory(self):
        attributes = {"AttribA": Attribute("AttribA", {"AttribA": 44})}
        specifications = new_specs(
            [
                new_attribute(
                    "AttribA",
                    "block",
                    True,
                    False,
                    [new_attribute("AttribB", "double", True, False, [])],
                )
            ]
        )
        with pytest.raises(ValidationException) as e_info:
            SchemaValidator._ensure_mandatory_present(attributes, specifications)
        assert_exception_contains(SchemaValidator._ATTRIBUTE_MISSING, e_info)

    def test_ensure_mandatory_is_present_nested_list_missing_mandatory(self):
        attributes = {"AttribA": Attribute("AttribA", [{"AttribB": 44}, {"AttribA": 22}])}
        specifications = new_specs(
            [
                new_attribute(
                    "AttribA",
                    "block",
                    True,
                    True,
                    [new_attribute("AttribB", "double", True, False, [])],
                )
            ]
        )
        with pytest.raises(ValidationException) as e_info:
            SchemaValidator._ensure_mandatory_present(attributes, specifications)
        assert_exception_contains(SchemaValidator._ATTRIBUTE_MISSING, e_info)

    def test_ensure_mandatory_is_present_nested_missing_optional(self):
        attributes = {"AttribA": Attribute("AttribA", {"AttribA": 44})}
        specifications = new_specs(
            [
                new_attribute(
                    "AttribA",
                    "block",
                    True,
                    False,
                    [new_attribute("AttribB", "double", False, False, [])],
                )
            ]
        )
        SchemaValidator._ensure_mandatory_present(attributes, specifications)

    def test_ensure_attributes_exist_no_nested(self):
        attributes = {
            "AttribA": Attribute("AttribA", 55),
            "AttribB": Attribute("AttribB", 44),
        }
        specifications = new_specs(
            [
                new_attribute("AttribA", "double", True, False, []),
                new_attribute("AttribB", "double", False, False, []),
            ]
        )
        SchemaValidator._ensure_attributes_exist(attributes, specifications)

    def test_ensure_attributes_exist_nested(self):
        attributes = {"AttribA": Attribute("AttribA", {"AttribB": 44})}
        specifications = new_specs(
            [
                new_attribute(
                    "AttribA",
                    "block",
                    True,
                    False,
                    [new_attribute("AttribB", "double", True, False, [])],
                )
            ]
        )
        SchemaValidator._ensure_attributes_exist(attributes, specifications)

    def test_ensure_attributes_exist_missing_no_nested(self):
        attributes = {
            "AttribA": Attribute("AttribA", 55),
            "AttribB": Attribute("AttribB", 44),
        }
        specifications = new_specs([new_attribute("AttribA", "double", True, False, [])])
        with pytest.raises(ValidationException) as e_info:
            SchemaValidator._ensure_attributes_exist(attributes, specifications)
        assert_exception_contains(SchemaValidator._ATTRIBUTE_UNKNOWN, e_info)

    def test_ensure_attributes_exist_missing_nested(self):
        attributes = {"AttribA": Attribute("AttribA", {"AttribB": 44})}
        specifications = new_specs([new_attribute("AttribA", "block", True, False, [])])
        with pytest.raises(ValidationException) as e_info:
            SchemaValidator._ensure_attributes_exist(attributes, specifications)
        assert_exception_contains(SchemaValidator._ATTRIBUTE_UNKNOWN, e_info)

    def test_ensure_attributes_exist_missing_nested_list(self):
        attributes = {"AttribA": Attribute("AttribA", [{"AttribB": 44}])}
        specifications = new_specs([new_attribute("AttribA", "block", True, True, [])])
        with pytest.raises(ValidationException) as e_info:
            SchemaValidator._ensure_attributes_exist(attributes, specifications)
        assert_exception_contains(SchemaValidator._ATTRIBUTE_UNKNOWN, e_info)

    def test_ensure_value_matches_type_no_nested(self):
        attributes = {"AttribA": Attribute("", 55), "AttribB": Attribute("", 44.0)}
        specifications = new_specs(
            [
                new_attribute("AttribA", "integer", True, False, []),
                new_attribute("AttribB", "double", False, False, []),
            ]
        )
        SchemaValidator._ensure_value_matches_type(attributes, specifications)

    def test_ensure_matches_type_no_nested_mismatch(self):
        attributes = {"AttribA": Attribute("", "Not a Double")}
        specifications = new_specs([new_attribute("AttribA", "double", True, False, [])])
        with pytest.raises(ValidationException) as e_info:
            SchemaValidator._ensure_value_matches_type(attributes, specifications)
        assert_exception_contains(SchemaValidator._INCOMPATIBLE, e_info)

    def test_ensure_matches_type_no_nested_disallowed(self):
        attributes = {"AttribA": Attribute("AttribA", 0)}
        specifications = new_specs([new_attribute("AttribA", "double", True, False, None, [42.0])])
        with pytest.raises(ValidationException) as e_info:
            SchemaValidator._ensure_value_matches_type(attributes, specifications)
        assert_exception_contains(SchemaValidator._DISALLOWED, e_info)

    def test_ensure_matches_type_no_nested_allowed(self):
        attributes = {"AttribA": Attribute("AttribA", 21)}
        specifications = new_specs([new_attribute("AttribA", "double", True, False, None, [21.0])])
        SchemaValidator._ensure_value_matches_type(attributes, specifications)

    def test_ensure_matches_type_nested_mismatch(self):
        attributes = {"AttribA": Attribute("AttribA", {"AttribB": "Not a double"})}
        specifications = new_specs(
            [
                new_attribute(
                    "AttribA",
                    "block",
                    True,
                    False,
                    [new_attribute("AttribB", "double", True, False, [])],
                )
            ]
        )
        with pytest.raises(ValidationException) as e_info:
            SchemaValidator._ensure_value_matches_type(attributes, specifications)
        assert_exception_contains(SchemaValidator._INCOMPATIBLE, e_info)

    def test_ensure_matches_type_nested_disallowed(self):
        attributes = {"AttribA": Attribute("AttribA", {"AttribB": -5.2})}
        specifications = new_specs(
            [
                new_attribute(
                    "AttribA",
                    "block",
                    True,
                    False,
                    [new_attribute("AttribB", "double", True, False, None, [42.0])],
                )
            ]
        )
        with pytest.raises(ValidationException) as e_info:
            SchemaValidator._ensure_value_matches_type(attributes, specifications)
        assert_exception_contains(SchemaValidator._DISALLOWED, e_info)

    def test_ensure_matches_type_nested_allowed(self):
        attributes = {"AttribA": Attribute("AttribA", {"AttribB": -2})}
        specifications = new_specs(
            [
                new_attribute(
                    "AttribA",
                    "block",
                    True,
                    False,
                    [new_attribute("AttribB", "integer", True, False, None, [5, -2, 99])],
                )
            ]
        )
        SchemaValidator._ensure_value_matches_type(attributes, specifications)

    def test_ensure_matches_type_nested_list_allowed(self):
        attributes = {"AttribA": Attribute("AttribA", [{"InnerA": -1, "InnerB": 1}, {"InnerA": -2, "InnerB": 2}])}
        specifications = new_specs(
            [
                new_attribute(
                    "AttribA",
                    "block",
                    True,
                    True,
                    [
                        new_attribute("InnerA", "integer", True, False, None, [-1, -2]),
                        new_attribute("InnerB", "integer", True, False, None, [1, 2]),
                    ],
                )
            ]
        )
        SchemaValidator._ensure_value_matches_type(attributes, specifications)

    def test_ensure_matches_type_nested_list_disallowed(self):
        attributes = {"AttribA": Attribute("AttribA", [{"InnerA": -5, "InnerB": 1}, {"InnerA": -2, "InnerB": 2}])}
        specifications = new_specs(
            [
                new_attribute(
                    "AttribA",
                    "block",
                    True,
                    True,
                    [
                        new_attribute("InnerA", "integer", True, False, None, [-1, -2]),
                        new_attribute("InnerB", "integer", True, False, None, [1, 2]),
                    ],
                )
            ]
        )
        with pytest.raises(ValidationException) as e_info:
            SchemaValidator._ensure_value_matches_type(attributes, specifications)
        assert_exception_contains(SchemaValidator._DISALLOWED, e_info)

    def test_ensure_matches_type_nested_list_type_mismatch(self):
        attributes = {"AttribA": Attribute("AttribA", [{"InnerA": 99.5}])}
        specifications = new_specs(
            [
                new_attribute(
                    "AttribA",
                    "block",
                    True,
                    True,
                    [new_attribute("InnerA", "integer", True, False, None, [-1, -2])],
                )
            ]
        )
        with pytest.raises(ValidationException) as e_info:
            SchemaValidator._ensure_value_matches_type(attributes, specifications)
        assert_exception_contains(SchemaValidator._INCOMPATIBLE, e_info)

    @staticmethod
    def assert_compatible_val(attribute_type: AttributeType, expected: bool, values_to_test: list) -> None:
        """Asserts that call to _is_compatible() for  `attribute_type` and each `value_to_test` results in `expected`"""
        for value_to_test in values_to_test:
            assert SchemaValidator._is_compatible_value(attribute_type, value_to_test) is expected

    def test_is_compatible_value_integer(self):
        Test.assert_compatible_val(AttributeType.INTEGER, True, [22, 0, -15])
        Test.assert_compatible_val(
            AttributeType.INTEGER,
            False,
            [-2147483648, 2147483647, 5.0, "5", {"A": 5}, [2, 3]],
        )

    def test_is_compatible_value_long(self):
        Test.assert_compatible_val(AttributeType.LONG, True, [22, 0, -15, -2147483648, 2147483647])
        Test.assert_compatible_val(AttributeType.LONG, False, [5.0, "5", {"A": 5}, [2, 3]])

    def test_is_compatible_value_double(self):
        Test.assert_compatible_val(AttributeType.DOUBLE, True, [22.0, 0.0, -15.0, -5, 7])
        Test.assert_compatible_val(AttributeType.DOUBLE, False, ["5", {"A": 5}, [2, 3]])

    def test_is_compatible_value_time_stamp(self):
        Test.assert_compatible_val(
            AttributeType.TIME_STAMP,
            True,
            [100, -50, "-200", "150", "2000-09-01_15:26:12"],
        )
        Test.assert_compatible_val(
            AttributeType.TIME_STAMP,
            False,
            ["LaLaLa", "20-9-1_15:26:12", {"A": 5}, [2, 3]],
        )

    def test_is_compatible_value_string(self):
        Test.assert_compatible_val(AttributeType.STRING, True, ["a string", "anotherString"])
        Test.assert_compatible_val(AttributeType.STRING, False, [["String", "AnotherString"], 5, 5.0, {"A": 5}])

    def test_is_compatible_value_enum(self):
        Test.assert_compatible_val(AttributeType.ENUM, True, ["a string"])
        Test.assert_compatible_val(AttributeType.ENUM, False, [["String", "AnotherString"], 5, 5.0, {"A": 5}])

    def test_is_compatible_value_time_series(self):
        Test.assert_compatible_val(AttributeType.TIME_SERIES, True, ["a string", 5, 6.0])
        Test.assert_compatible_val(
            AttributeType.TIME_SERIES,
            False,
            [["String", "AnotherString"], [5, 6], {"A": 5}],
        )

    def test_is_compatible_list_is_no_list_but_compatible(self):
        specification = new_specs([new_attribute("AttribA", "enum", True, True)])["AttribA"]
        assert SchemaValidator._is_compatible(specification, "Not a list but compatible")

    def test_is_compatible_list_is_no_list_but_not_compatible(self):
        specification = new_specs([new_attribute("AttribA", "double", True, True)])["AttribA"]
        assert not SchemaValidator._is_compatible(specification, "Not a list and not double")

    def test_is_compatible_list_is_list_but_not_all_compatible(self):
        specification = new_specs([new_attribute("AttribA", "double", True, True)])["AttribA"]
        assert not SchemaValidator._is_compatible(specification, [5, 2, 5, "No double", 22])

    def test_is_compatible_list_is_list_all_compatible(self):
        specification = new_specs([new_attribute("AttribA", "double", True, True)])["AttribA"]
        assert SchemaValidator._is_compatible(specification, [5, 2, 5, 22])

    def test_is_compatible_no_list_but_list_given(self):
        specification = new_specs([new_attribute("AttribA", "double", True, False)])["AttribA"]
        assert not SchemaValidator._is_compatible(specification, [5, 2, 5, 22])

    def test_is_compatible_no_list_not_compatible(self):
        specification = new_specs([new_attribute("AttribA", "double", True, False)])["AttribA"]
        assert not SchemaValidator._is_compatible(specification, "Not a double")

    def test_is_compatible_no_list_compatible(self):
        specification = new_specs([new_attribute("AttribA", "double", True, False)])["AttribA"]
        assert SchemaValidator._is_compatible(specification, 42)

    def test_ensure_is_valid_contract(self):
        contract = new_contract(1, 2, "ProductA")
        schema = Schema.from_dict(new_schema([new_agent("MyAgent", [], ["ProductA"])]))
        agent_types_by_id = {1: "MyAgent", 2: "MyAgent"}
        SchemaValidator.ensure_is_valid_contract(contract, schema, agent_types_by_id)

    def test_ensure_is_valid_contract_missing_sender(self):
        contract = new_contract(1, 2, "ProductA")
        schema = Schema.from_dict(new_schema([new_agent("MyAgent", [], ["ProductA"])]))
        agent_types_by_id = {2: "MyAgent"}
        with pytest.raises(ValidationException) as e_info:
            SchemaValidator.ensure_is_valid_contract(contract, schema, agent_types_by_id)
        assert_exception_contains(SchemaValidator._AGENT_MISSING, e_info)

    def test_ensure_is_valid_contract_missing_receiver(self):
        contract = new_contract(1, 2, "ProductA")
        schema = Schema.from_dict(new_schema([new_agent("MyAgent", [], ["ProductA"])]))
        agent_types_by_id = {1: "MyAgent"}
        with pytest.raises(ValidationException) as e_info:
            SchemaValidator.ensure_is_valid_contract(contract, schema, agent_types_by_id)
        assert_exception_contains(SchemaValidator._AGENT_MISSING, e_info)

    def test_ensure_is_valid_contract_unknown_sender_type(self):
        contract = new_contract(1, 2, "ProductA")
        schema = Schema.from_dict(new_schema([new_agent("MyAgent", [], ["ProductA"])]))
        agent_types_by_id = {1: "MissingAgentType", 2: "MyAgent"}
        with pytest.raises(ValidationException) as e_info:
            SchemaValidator.ensure_is_valid_contract(contract, schema, agent_types_by_id)
        assert_exception_contains(SchemaValidator._AGENT_TYPE_UNKNOWN, e_info)

    def test_ensure_is_valid_contract_missing_product(self):
        contract = new_contract(1, 2, "MissingProduct")
        schema = Schema.from_dict(new_schema([new_agent("MyAgent", [], ["ProductA"])]))
        agent_types_by_id = {1: "MyAgent", 2: "MyAgent"}
        with pytest.raises(ValidationException) as e_info:
            SchemaValidator.ensure_is_valid_contract(contract, schema, agent_types_by_id)
        assert_exception_contains(SchemaValidator._PRODUCT_MISSING, e_info)

    def test_ensure_is_valid_scenario(self):
        agents = [Agent(1, "MyAgent"), Agent(2, "MyAgent"), Agent(3, "MyAgent")]
        SchemaValidator.ensure_unique_agent_ids(agents)

    def test_ensure_is_valid_scenario_one_duplicate(self):
        agents = [Agent(1, "MyAgent"), Agent(2, "MyAgent"), Agent(1, "MyAgent")]
        with pytest.raises(ValidationException) as e_info:
            SchemaValidator.ensure_unique_agent_ids(agents)
        assert_exception_contains(SchemaValidator._AGENT_ID_NOT_UNIQUE, e_info)

    def test_ensure_is_valid_scenario_two_duplicate(self):
        agents = [
            Agent(1, "MyA"),
            Agent(2, "MyA"),
            Agent(1, "MyA"),
            Agent(3, "MyA"),
            Agent(2, "MyA"),
        ]
        with pytest.raises(ValidationException) as e_info:
            SchemaValidator.ensure_unique_agent_ids(agents)
        assert_exception_contains(SchemaValidator._AGENT_ID_NOT_UNIQUE, e_info)

    def test_ensure_agent_type_in_schema(self):
        schema = Schema.from_dict(new_schema([new_agent("MyAgent", [], ["ProductA"])]))
        agent = Agent(1, "MyAgent")
        SchemaValidator.ensure_agent_type_in_schema(agent, schema)

    def test_ensure_agent_type_in_schema_unknown_in_schema(self):
        schema = Schema.from_dict(new_schema([new_agent("UNKNOWN_AGENT_TYPE", [], ["ProductA"])]))
        agent = Agent(1, "MyAgent")
        with pytest.raises(ValidationException) as e_info:
            SchemaValidator.ensure_agent_type_in_schema(agent, schema)
        assert_exception_contains(SchemaValidator._AGENT_TYPE_UNKNOWN, e_info)
