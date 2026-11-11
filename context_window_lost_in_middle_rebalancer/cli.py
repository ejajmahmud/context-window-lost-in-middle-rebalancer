"""CLI for context-window-lost-in-middle-rebalancer."""
import sys
import argparse
from .rebalancer import ContextRebalancer, PrioritizedDocument

def main():
    parser = argparse.ArgumentParser(description="Context Window Lost-in-Middle Rebalancer CLI")
    parser.add_argument("--demo", action="store_true", help="Rebalance sample scored documents")
    args = parser.parse_args()

    if args.demo:
        reb = ContextRebalancer()
        docs = [
            PrioritizedDocument("D1", "Best doc", 0.99),
            PrioritizedDocument("D2", "2nd best", 0.90),
            PrioritizedDocument("D3", "3rd best", 0.80),
            PrioritizedDocument("D4", "4th best", 0.70),
            PrioritizedDocument("D5", "5th best", 0.60)
        ]
        out = reb.rebalance(docs)
        print("Rebalanced U-Shaped Order:")
        for idx, d in enumerate(out):
            print(f"  Pos {idx}: {d.doc_id} (Score: {d.relevance_score})")
    else:
        parser.print_help()
    sys.exit(0)

if __name__ == "__main__":
    main()
