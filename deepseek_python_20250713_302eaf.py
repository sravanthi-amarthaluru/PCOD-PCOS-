# Modified to use relative imports
import sys
from pathlib import Path

# Add the parent directory to Python path
sys.path.append(str(Path(__file__).parent))

# Now import your modules
try:
    from auth.core import initialize_session
except ImportError as e:
    st.error(f"Import Error: {e}")
    st.stop()

import streamlit as st

def main():
    initialize_session()
    st.title("FemCare Health")

if __name__ == "__main__":
    main()