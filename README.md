# Code for Fun

Small, guided exercises for practicing AI-assisted development with Cline.

## Recommended workshop exercise

### Manufacturing Quality Checker

Build a Python command-line tool that reads production-line sensor data from a
CSV file, checks each item against quality thresholds, and prints a shift
summary.

This exercise is intentionally small:

- one Python starter file
- one sample CSV file
- Python standard library only
- two focused TODO sections
- no package installation

Start here:

```bash
cd manufacturing-quality-checker
python3 starter/quality_checker.py
```

The starter will stop at the first unfinished TODO. Open
`starter/quality_checker.py`, give Cline the prompt in the file, confirm that
it changes only the two TODO sections, and run the command again.

An instructor reference implementation is available in
`solution/quality_checker.py`. Use it only after attempting the starter:

```bash
python3 solution/quality_checker.py
```

## Possible future exercises

- **Financial transaction risk checker**: flag transactions using amount,
  country, and repeated-attempt rules.
- **Loan payment calculator**: calculate monthly payment and total interest
  from principal, annual rate, and term.
- **Inventory reorder advisor**: compare stock, daily usage, and supplier lead
  time to recommend reorder quantities.
- **Machine downtime analyzer**: summarize downtime events by machine and
  reason from a CSV file.
- **Energy anomaly detector**: flag factory equipment whose power consumption
  exceeds a fixed baseline.
