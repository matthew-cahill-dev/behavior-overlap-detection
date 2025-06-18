import json
from utils import find_exact_duplicates, find_similar_behaviors, find_conflicts

def load_local_behaviors(filepath="sample_behaviors.json"):
    """Load behaviors from local JSON file for offline testing"""
    with open(filepath, "r") as f:
        data = json.load(f)
    return data

def main():
    print("📂 Loading local sample behaviors...")
    behaviors = load_local_behaviors()

    print(f"✅ Total behaviors loaded: {len(behaviors)}")

    print("\n🔍 Checking for exact duplicates...")
    duplicates = find_exact_duplicates(behaviors)
    for a, b in duplicates:
        print(f"Duplicate found:\n - ID {a['id']}: {a['description']}\n - ID {b['id']}: {b['description']}")

    print("\n🤝 Checking for similar behaviors...")
    similar = find_similar_behaviors(behaviors)
    for a, b, score in similar:
        print(f"Possible overlap ({score}% similar):\n - ID {a['id']}: {a['description']}\n - ID {b['id']}: {b['description']}")

    print("\n⚡ Checking for toy conflicts...")
    conflicts = find_conflicts(behaviors)
    for b in conflicts:
        print(f"Potential conflict in ID {b['id']}: {b['description']}")

    print("\n🎉 Done!")

if __name__ == "__main__":
    main()
