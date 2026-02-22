import os, sys, glob, subprocess
d = "xmindFilesToBeConverted"
files = glob.glob(os.path.join(d, '*.xmind'))
if not files:
    print("No .xmind files found in", d)
else:
    for f in files:
        print("Converting:", f)
        try:
            subprocess.run(["xmindparser", f, "-markdown"], check=True)
        except FileNotFoundError:
            print("`xmindparser` CLI not found; installing package...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", "xmindparser"])
            subprocess.run(["xmindparser", f, "-markdown"], check=True)
        except subprocess.CalledProcessError as e:
            print("Conversion failed for", f, ":", e)
