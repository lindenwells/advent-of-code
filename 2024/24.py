from get_input import get_input
from dataclasses import dataclass
from enum import Enum

class Gate(Enum):
    xor_gate = 0
    and_gate = 1
    or_gate = 2

@dataclass
class WireAttributes:
    wire_type = "attributes"
    a: str
    b: str
    gate: Gate

@dataclass
class InitialValue:
    wire_type = "initial_value"
    value: int


network: dict[str, WireAttributes | InitialValue] = {

}

inputs = [line.strip() for line in get_input(day=24)]

# should be an empty string where the initial values end and the network layout begins
index_of_separator = inputs.index('')
initial_values = inputs[:index_of_separator]
connections = inputs[index_of_separator + 1: ]

def parse_gate(gate: str) -> Gate:
    if gate == "XOR":
        return Gate.xor_gate
    if gate == "OR":
        return Gate.or_gate
    if gate == "AND":
        return Gate.and_gate
    print("oh nmo")

for line in initial_values:
    wire, value = line.split(": ")
    network[wire] = InitialValue(value=int(value))

for line in connections:
    rest, out_wire = line.split(" -> ")
    in_wire_1, gate, in_wire_2 = rest.split(" ")
    network[out_wire] = WireAttributes(a=in_wire_1, b=in_wire_2, gate=parse_gate(gate))

def output(wire: str) -> int:
    attributes = network[wire]
    if attributes.wire_type == "initial_value":
        return attributes.value
    
    if attributes.gate == Gate.and_gate:
        return output(attributes.a) & output(attributes.b)
    elif attributes.gate == Gate.xor_gate:
        return output(attributes.a) ^ output(attributes.b)
    elif attributes.gate == Gate.or_gate:
        return output(attributes.a) | output(attributes.b)
    
    print("oh bjorn!")
    
output_wires = list(reversed(sorted(list(filter(lambda key: key.startswith("z"), network.keys())))))

print("".join([str(int(output(wire))) for wire in output_wires]))
