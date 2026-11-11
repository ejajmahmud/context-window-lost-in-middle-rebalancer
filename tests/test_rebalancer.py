"""Unit tests for context-window-lost-in-middle-rebalancer."""
import unittest
from context_window_lost_in_middle_rebalancer.rebalancer import ContextRebalancer, PrioritizedDocument

class TestContextRebalancer(unittest.TestCase):
    def setUp(self):
        self.reb = ContextRebalancer()

    def test_u_shape_distribution(self):
        docs = [
            PrioritizedDocument("D1", "text", 10.0),
            PrioritizedDocument("D2", "text", 9.0),
            PrioritizedDocument("D3", "text", 8.0),
            PrioritizedDocument("D4", "text", 7.0),
            PrioritizedDocument("D5", "text", 6.0),
        ]
        res = self.reb.rebalance(docs)
        # Position 0 should be D1 (highest)
        self.assertEqual(res[0].doc_id, "D1")
        # Last position should be D2 (second highest)
        self.assertEqual(res[-1].doc_id, "D2")
        # Middle should contain D5 (lowest)
        self.assertEqual(res[2].doc_id, "D5")
