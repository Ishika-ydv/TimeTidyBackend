{ pkgs ? import <nixpkgs> {} }:

let
  pythonEnv = pkgs.python311.withPackages (ps: with ps; [
    pip
    setuptools
    wheel
    fastapi
    uvicorn
    python-dotenv
    pydantic
  ]);
in

pkgs.mkShell {
  buildInputs = [
    pythonEnv
    pkgs.nodejs_18
  ];

  shellHook = ''
    echo "✅ Custom Python 3.11 environment loaded"
  '';
}
