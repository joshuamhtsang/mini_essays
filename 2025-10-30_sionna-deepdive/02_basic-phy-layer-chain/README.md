# Basic Physical Layer Communication Chains

## Resources

[Sionna Physical Layer Tutorial Part 1](https://nvlabs.github.io/sionna/phy/tutorials/Sionna_tutorial_part1.html#Imports-&-Basics)

[Sionna API Documentation for Demapper Class](https://nvlabs.github.io/sionna/phy/api/mapping.html#sionna.phy.mapping.Demapper)

[Sionna API Documentation for ebnodb2no Function](https://nvlabs.github.io/sionna/phy/api/utils.html#sionna.phy.utils.ebnodb2no)

## Simple Physical Layer Chains

A Sionna physical layer chain involves several basic steps:

1. Generating data bits
2. Mapping the data bits to symbols
3. Passing the symbols through a channel to add noise
4. Demapping the noisy symbols back into data bits

The important objects are shown in the figure below.

![image](./images/basic_sionna_objects.png)

## No Noisy Channel

The figure below shows the components that compose a basic physical layer chain works in Sionna. Note this isn't using the concept of Sionna blocks yet.

![image](./images/basic_sionna_chain.png)

## Adding a Noisy Channel

- Compute a noise variance, `no`, for a given EbN0 ratio using the function `ebnodb2no()`.

![image](./images/basic_sionna_chain_with_channel.png)

- `llr` is the log-likelihood ratio tensor.
- To output hard bit decisions from `llr` there are 2 options: using the `hard_out` option in the Demapper or use the utility function `hard_decisions()`.

The figure below shows the amount of noise introduced into the constellation for different values of `ebno`.

![image](./images/constellation_vs_ebno.png)

You can see that at `ebno` = -3 dB it's not even clear that we are using 4-QAM.

## BER vs `ebno` plot

![iamge](./images/ber_vs_ebno.png)