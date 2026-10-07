class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        queue = [0]
        visited = set([0])

        while queue:
            room = queue.pop()

            for key in rooms[room]:
                if key not in visited:
                    queue.append(key)
                    visited.add(key)

        return len(rooms) == len(visited)
