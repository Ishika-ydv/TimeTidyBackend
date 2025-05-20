{ pkgs ? import <nixpkgs> {} }:

let
  pythonEnv = pkgs.python311.withPackages (ps: with ps; [
    pip
    setuptools
    wheel
  ]);
in

pkgs.mkShell {
  buildInputs = [
    pythonEnv
    pkgs.nodejs_18
  ];

  shellHook = ''
    # Create a virtual environment in the root directory
    python3 -m venv ./venv
    # Activate the virtual environment
    source ./venv/bin/activate
    echo "✅ Custom Python 3.11 environment and virtual environment loaded"
  '';
}
