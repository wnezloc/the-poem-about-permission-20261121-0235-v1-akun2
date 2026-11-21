import os

POEM = """You handed me the keys
and stayed beside the door.
Not watching, exactly —
just near enough that yes
could still reach me.
That is the whole of it:
power is not the keys.
It is the hand that stays."""

def main():
    assert 1 <= len(POEM) <= 280, "poem must be 1-280 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.txt")
    with open(dst, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)
    print(f"wrote {dst}: {len(POEM)} characters")

if __name__ == "__main__":
    main()
