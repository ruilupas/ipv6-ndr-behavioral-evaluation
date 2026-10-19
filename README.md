# ipv6-ndr-behavioral-evaluation
Experimental framework, traffic simulation scripts, and evaluation metrics for AI-based NDR detection across IPv4 and IPv6.

# Behavioral Anomaly Detection in Dual-Stack Networks: Evaluating AI-Based Detection Across IPv4 and IPv6

This repository contains the experimental framework, traffic generation scripts, and evaluation metrics associated with the research paper: **"Behavioral Anomaly Detection in Dual-Stack Networks: Evaluating AI-Based Detection Across IPv4 and IPv6"**.

## Abstract
This study evaluates whether commercial AI-based Network Detection and Response (NDR) platforms (specifically Darktrace) can identify anomalous and malicious behavior in IPv6 traffic as effectively as in IPv4 traffic, within a controlled dual-stack testbed environment.

## Repository Structure
- `scripts/`: Contains Python scripts (using Scapy and system utilities) used to simulate equivalent attack scenarios (Reconnaissance, C2 Beaconing, Exfiltration, NDP anomalies, and IPv6 Address Churn).
- `results/`: Contains raw CSV data and metrics corresponding to the evaluation scenarios presented in the paper (Detection Rates, False Positives, and Latency).

## Usage & Requirements
The scripts are intended for execution **exclusively inside an isolated, non-production testbed** under administrative control.

Dependencies:
- Python 3.x
- Scapy library (`pip install scapy`)

## Citation
If you use this work or code in your research, please cite our paper:
> R. Pascoal and N. Galego, "Behavioral Anomaly Detection in Dual-Stack Networks: Evaluating AI-Based Detection Across IPv4 and IPv6," 2026.
