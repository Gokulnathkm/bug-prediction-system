from pydriller import Repository
import pandas as pd
from radon.complexity import cc_visit
import os, re

def extract_features(repo_path, output_csv="data/processed/features.csv"):
    print(f"Mining repo: {repo_path}")
    print("This may take 2–5 minutes...")

    file_stats = {}

    for commit in Repository(repo_path).traverse_commits():
        is_bugfix = bool(re.search(
            r'\b(fix|bug|defect|error|issue|crash|fail|patch|hotfix)\b',
            commit.msg.lower()
        ))

        for mod in commit.modified_files:
            if not mod.filename.endswith(".py"):
                continue

            fname = mod.filename

            if fname not in file_stats:
                file_stats[fname] = {
                    "filename": fname,
                    "total_changes": 0,
                    "total_lines_added": 0,
                    "total_lines_deleted": 0,
                    "complexity_sum": 0,
                    "complexity_count": 0,
                    "loc_sum": 0,
                    "loc_count": 0,
                    "authors": set(),
                    "bug_fix_commits": 0
                }

            s = file_stats[fname]
            s["total_changes"] += 1
            s["total_lines_added"] += mod.added_lines
            s["total_lines_deleted"] += mod.deleted_lines
            s["authors"].add(commit.author.name)

            if mod.source_code:
                try:
                    blocks = cc_visit(mod.source_code)
                    if blocks:
                        s["complexity_sum"] += sum(b.complexity for b in blocks)
                        s["complexity_count"] += 1
                except:
                    pass

            if mod.nloc:
                s["loc_sum"] += mod.nloc
                s["loc_count"] += 1

            if is_bugfix:
                s["bug_fix_commits"] += 1

    # Build final dataframe
    rows = []
    for fname, s in file_stats.items():
        rows.append({
            "filename": fname,
            "total_changes": s["total_changes"],
            "total_lines_added": s["total_lines_added"],
            "total_lines_deleted": s["total_lines_deleted"],
            "avg_complexity": round(s["complexity_sum"] / s["complexity_count"], 2)
                              if s["complexity_count"] > 0 else 0,
            "avg_loc": round(s["loc_sum"] / s["loc_count"], 2)
                       if s["loc_count"] > 0 else 0,
            "num_authors": len(s["authors"]),
            "bug_fix_commits": s["bug_fix_commits"],
            "label": 1 if s["bug_fix_commits"] > 0 else 0
        })

    df = pd.DataFrame(rows)
    os.makedirs("data/processed", exist_ok=True)
    df.to_csv(output_csv, index=False)

    print(f"\nDone! {len(df)} files extracted.")
    print(f"Buggy files (label=1): {df['label'].sum()}")
    print(f"Clean files (label=0): {(df['label']==0).sum()}")
    print(f"Saved to: {output_csv}")
    return df

if __name__ == "__main__":
    extract_features("data/raw/requests")

    