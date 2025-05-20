{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
  pkgs.python311Full
  pkgs.nodejs_18
  pkgs.python311Packages.pip
  pkgs.python311Packages.setuptools
  pkgs.python311Packages.wheel
];


  shellHook = ''
    echo "✅ Custom Nix environment loaded"
  '';
}
