from xonsh.built_ins import XSH

def _load_xontrib_(xsh, **kwargs):
    xsh.builtins.events.on_transform_command(dotdot_transform)

def dotdot_transform(cmd: str) -> str:
    cmd = cmd.strip()
    use_commas = XSH.env.get('XONTRIB_DOTDOT_COMMA', True)
    if cmd.count('.') + (cmd.count(',') if use_commas else 0) == len(cmd) and len(cmd) >= 2:
        return "cd " + "../" * (len(cmd) - 1)
    return cmd + "\n"
