from difflib import SequenceMatcher

def find_exact_duplicates(behaviors):
    """Find behaviors with identical descriptions"""
    duplicates = []
    seen = {}
    for b in behaviors:
        desc = b['description'].strip().lower()
        if desc in seen:
            duplicates.append((seen[desc], b))
        else:
            seen[desc] = b
    return duplicates

def find_similar_behaviors(behaviors, threshold=0.8):
    """Find pairs of behaviors with high similarity"""
    similar_pairs = []
    for i in range(len(behaviors)):
        for j in range(i + 1, len(behaviors)):
            desc1 = behaviors[i]['description']
            desc2 = behaviors[j]['description']
            ratio = SequenceMatcher(None, desc1, desc2).ratio()
            if threshold < ratio < 1.0:
                similar_pairs.append((behaviors[i], behaviors[j], round(ratio * 100, 2)))
    return similar_pairs

def find_conflicts(behaviors):
    """Toy example: flag if a single behavior says both always and never"""
    conflicts = []
    for b in behaviors:
        desc = b['description'].lower()
        if "always" in desc and "never" in desc:
            conflicts.append(b)
    return conflicts
