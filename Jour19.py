class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head) -> bool:
    """
    Détecte si une liste chaînée contient un cycle (Floyd - tortue/lièvre).

    Paramètres:
        head (ListNode): tête de la liste chaînée

    Retourne:
        bool: True s'il existe un cycle, False sinon
    """
    slow = head
    fast = head

    # Tant qu’on peut avancer
    while fast and fast.next:
        slow = slow.next          # avance de 1
        fast = fast.next.next     # avance de 2
        print(f"Slow: {slow.val if slow else None}, Fast: {fast.val if fast else None}")

        if slow == fast:
            return True           # La tortue et le lièvre se rencontrent → cycle

    return False                  # fast a rencontré None → pas de cycle



if __name__ == "__main__":
    # 3 → 2 → 0 → -4 → (retour vers 2)
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2   # cycle

    print(hasCycle(node1))   # True