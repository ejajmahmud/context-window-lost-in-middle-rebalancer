"""Core Context Rebalancer implementation."""
from dataclasses import dataclass
from typing import Any, List

@dataclass
class PrioritizedDocument:
    doc_id: str
    content: str
    relevance_score: float

class ContextRebalancer:
    """Rebalances documents in a U-shaped distribution to counteract the Lost-in-the-Middle attention bias."""
    
    def rebalance(self, documents: List[PrioritizedDocument]) -> List[PrioritizedDocument]:
        """Arranges documents so the highest relevance docs appear at the beginning and the end."""
        # 1. Sort descending by relevance
        sorted_docs = sorted(documents, key=lambda d: d.relevance_score, reverse=True)
        if len(sorted_docs) <= 2:
            return sorted_docs

        rebalanced = [None] * len(sorted_docs)
        left = 0
        right = len(sorted_docs) - 1

        # Alternate placing highest remaining items at the left (head) and right (tail)
        for i, doc in enumerate(sorted_docs):
            if i % 2 == 0:
                rebalanced[left] = doc
                left += 1
            else:
                rebalanced[right] = doc
                right -= 1

        return rebalanced
