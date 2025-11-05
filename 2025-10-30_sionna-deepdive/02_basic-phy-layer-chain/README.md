# Basic Physical Layer Communication Chains

## Resources

[Sionna Physical Layer Tutorial Part 1](https://nvlabs.github.io/sionna/phy/tutorials/Sionna_tutorial_part1.html#Imports-&-Basics)

[Sionna API Documentation for Demapper Class](https://nvlabs.github.io/sionna/phy/api/mapping.html#sionna.phy.mapping.Demapper)

[Sionna API Documentation for ebnodb2no Function](https://nvlabs.github.io/sionna/phy/api/utils.html#sionna.phy.utils.ebnodb2no)

## Simple Physical Layer Chains

A Sionna physical layer chain involves several basic steps:

1. Generating data bits
2. Mapping the data bits to symbols
3. Passing the symbols through a channel
4. Demapping the symbols back into data bits

The important objects are shown below.

![image](./images/basic_sionna_objects.png)

## No Noisy Channel

![image](./images/basic_sionna_chain.png)

## Adding a Noisy Channel

![image](./images/basic_sionna_chain_with_channel.png)

## Demapper 'hard-out' Option

