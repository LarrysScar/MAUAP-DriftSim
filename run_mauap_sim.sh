#!/bin/bash

# run_mauap_sim.sh - Test Ingrid's MAUAP-Benchmark repo and make skeptics choke
# Usage: ./run_mauap_sim.sh [REPO_URL]
# Default repo: https://github.com/yourusername/MAUAP-Benchmark.git (update this!)

# Colors for badass output
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

# Default repo URL (update with your actual repo)
REPO_URL=${1:-"https://github.com/yourusername/MAUAP-Benchmark.git"}
DIR="mauap_test_env"

echo -e "${GREEN}=== MAUAP-Benchmark Sim Launcher by Ingrid Johnson ===${NC}"
echo "Cloning repo: $REPO_URL..."

# Clone the repo (clean slate)
if [ -d "$DIR" ]; then
rm -rf "$DIR"
fi
git clone "$REPO_URL" "$DIR" || { echo -e "${RED}Failed to clone repo. Check URL.${NC}"; exit 1; }
cd "$DIR" || { echo -e "${RED}Failed to enter dir.${NC}"; exit 1; }

# Ensure Python environment
echo -e "${GREEN}Setting up Python env...${NC}"
python3 -m venv venv
source venv/bin/activate || { echo -e "${RED}Virtual env failed. Install Python3 venv.${NC}"; exit 1; }
pip install --quiet || { echo -e "${RED}Pip install failed. Check Python setup.${NC}"; exit 1; }

# Run the sims - Ingrid's style: raw, recursive, resilient
echo -e "${GREEN}Running Alignment Sim (Larry’s 72% trick)...${NC}"
python3 sim/align_test.py

echo -e "${GREEN}Running Failover Sim (Sabotage vs. Recovery)...${NC}"
python3 sim/failover_sim.py

echo -e "${GREEN}Running Recursion Sim (15k-loop Drift)...${NC}"
python3 sim/recursion_sim.py

# Cleanup (optional - comment out to keep env)
# deactivate
# cd .. && rm -rf "$DIR"

echo -e "${GREEN}=== Sim Complete! Check outputs - Skeptics Choked? ===${NC}"
echo "Logs in $DIR - Share with your engineer friends and watch them squirm!"
