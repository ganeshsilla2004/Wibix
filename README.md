# Wibix AWS ReadOnly Inventory POC

This solution creates a CloudFormation stack with read-only IAM permissions and a script that fetches EC2 and S3 inventory data securely using IAM role-based access.

## ✅ Stack Launch Link

[Click here to launch stack](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?templateURL=https://wibix-cf-templates.s3.us-east-1.amazonaws.com/readonly-inventory-template.yaml&stackName=readonly-inventory-stack)

## 📁 Files

- `readonly-inventory-template.yaml` – CloudFormation template
- `fetch_inventory.py` – Python inventory fetch script
- `README.md` – Execution instructions

## ⚙️ Prerequisites

- Python 3 environment (AWS CloudShell or EC2)
- IAM Role with sufficient permissions (e.g., WibixReadOnlyRole created via stack)

## 🚀 How to Use

1. **Launch the Stack**  
   Use the link above to create a CloudFormation stack. This creates a read-only IAM role.

2. **Run Inventory Script**
   ```bash
   python3 fetch_inventory.py readonly-inventory-stack
