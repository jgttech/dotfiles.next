from subprocess import call
brew = "/home/linuxbrew/.linuxbrew/bin/brew"

call(f"{brew} install go odin zig rust lua luarocks", shell=True)
call(f"{brew} tap hashicorp/tap", shell=True)
call(f"{brew} install hashicorp/tap/terraform", shell=True)
