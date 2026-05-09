import os
import re
import glob

# markers of translationese
# 1. prepositions/conjunctions at start
start_markers = ["对于", "基于", "通过", "为了", "在", "由于", "尽管", "虽然", "随着", "当"]
# 2. stacked connectors
connectors = ["并且", "从而", "进而", "同时", "以及", "并", "且"]

def extract_sentences(text):
    # remove latex comments
    text = re.sub(r'%.*?(\n|$)', '', text)
    # roughly remove display math
    text = re.sub(r'\\begin\{equation\}.*?\\end\{equation\}', '', text, flags=re.DOTALL)
    text = re.sub(r'\\begin\{align\}.*?\\end\{align\}', '', text, flags=re.DOTALL)
    text = re.sub(r'\$\$.*?\$\$', '', text, flags=re.DOTALL)
    # remove commands like \cite{}, \ref{}, \figref{}, etc.
    text = re.sub(r'\\[a-zA-Z]+(\[.*?\])?\{.*?\}', '', text)
    # remove inline math roughly to avoid false positives
    text = re.sub(r'\$.*?\$', 'X', text)
    # split by punctuation
    sentences = re.split(r'[。！？]', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    return sentences

def score_sentence(sentence):
    score = 0
    reasons = []
    
    # Check length
    if len(sentence) > 60:
        score += 1
        reasons.append("Long sentence (>60 chars)")
        
    # Check starts
    for marker in start_markers:
        if sentence.startswith(marker) and len(sentence) > 30:
            # specifically look for trailing comma after a long intro
            if "，" in sentence:
                intro = sentence.split("，")[0]
                if len(intro) > 15:
                    score += 2
                    reasons.append(f"Long opening clause starting with '{marker}'")
                    break

    # Check stacked "的"
    de_count = sentence.count("的")
    if de_count >= 3:
        score += 1
        reasons.append(f"Multiple '的' ({de_count} times), indicating stacked pre-modifiers")
    if de_count >= 5:
        score += 2
        
    # Check stacked connectors
    conn_count = sum(sentence.count(c) for c in connectors)
    if conn_count >= 3:
        score += 1
        reasons.append(f"Stacked connectors ({conn_count} times)")

    # "在...下" or "在...中"
    if re.search(r'在.*?中，', sentence) or re.search(r'在.*?下，', sentence):
        score += 1
        reasons.append("Prepositional phrase framing ('在...中/下')")

    return score, reasons, sentence

results = []
files = glob.glob("**/*.tex", recursive=True)
for file in files:
    if "backup" in file or "post" in file or file.endswith("content.tex"):
        continue
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()
        sentences = extract_sentences(text)
        for s in sentences:
            if not re.search(r'[\u4e00-\u9fa5]', s):
                continue # not chinese
            score, reasons, clean_s = score_sentence(s)
            if score >= 3:
                results.append({
                    "file": file,
                    "sentence": clean_s,
                    "score": score,
                    "reasons": reasons
                })

results.sort(key=lambda x: x["score"], reverse=True)
for i, r in enumerate(results[:20]):
    print(f"File: {r['file']}")
    print(f"Score: {r['score']}")
    print(f"Sentence: {r['sentence']}")
    print(f"Reasons: {', '.join(r['reasons'])}")
    print("-" * 50)
