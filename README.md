# Credit Risk Modeling at Scale – Fannie Mae (Flagship Project)

## Business Context
Retail mortgage lenders must decide which loans to approve while minimizing Expected Credit Loss (ECL) and meeting regulatory constraints.

## Decision Problem
For each loan:
- Estimate Probability of Default (PD)
- Convert PD to Expected Loss
- Define approval / rejection threshold

## Data
Official public **Fannie Mae Single-Family Loan Performance Dataset**.
Due to size and regulatory realism, only a representative sample is stored here.

## Modeling Strategy
- Time-aware splits
- Missing value imputation
- Outlier treatment
- Interpretable baseline + calibrated PD

## Business Impact (Simulated (for demonstration))
- 18% reduction in Expected Loss
- Same approval rate
- Improved capital allocation

## Monitoring Considerations
- Vintage drift
- Macroeconomic regime change
- Calibration decay
