# Run setup beforehand
publish:
    #!/bin/bash
    source .env/bin/activate
    maturin publish -f -u __token__

# Setup venv and install maturin
setup:
    python -m venv .env
    .env/bin/pip install maturin

# Open python repl with package installed for testing
dev:
    #!/bin/bash
    source .env/bin/activate
    maturin develop
    python3