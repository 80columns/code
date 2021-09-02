using System;
using System.Collections.Generic;

namespace TowerOfHanoi {
    class Program {
        static int MoveDisks(
            Stack<int>[] _Rods,
            int _Source_Rod,
            int _Target_Rod,
            int _Disk_Count
        ) {
            var Move_Count = 0;

            if (_Disk_Count == 1) {
                var Disk = _Rods[_Source_Rod].Pop();
                _Rods[_Target_Rod].Push(Disk);
                Move_Count++;
            } else {
                // use 3 - (_SourceRod + _TargetRod) to get the unused rod
                var Temp_Rod = 3 - (_Source_Rod + _Target_Rod);

                Move_Count += MoveDisks(
                    _Rods,
                    _Source_Rod,
                    _Target_Rod: Temp_Rod,
                    _Disk_Count - 1
                );

                var Disk = _Rods[_Source_Rod].Pop();
                _Rods[_Target_Rod].Push(Disk);
                Move_Count++;

                Move_Count += MoveDisks(
                    _Rods,
                    _Source_Rod: Temp_Rod,
                    _Target_Rod,
                    _Disk_Count - 1
                );
            }

            return Move_Count;
        }

        /*
         * see https://en.wikipedia.org/wiki/Tower_of_Hanoi
         *
         * - Only one disk may be moved at a time.
         * - Each move consists of taking the upper disk from one of the stacks
         *   and placing it on top of another stack or on an empty rod.
         * - No disk may be placed on top of a disk that is smaller than it.
         */
        static void Main() {
            var Rods = new Stack<int>[3] {
                new Stack<int>(),
                new Stack<int>(),
                new Stack<int>()
            };
            var Disk_Count = 3;

            for (var i = Disk_Count; i > 0; i--) {
                Rods[0].Push(i);
            }

            // move all the disks from index 0 (1st rod) to index 2 (3rd rod)
            var Move_Count = MoveDisks(
                Rods,
                _Source_Rod: 0,
                _Target_Rod: 2,
                Disk_Count
            );

            Console.WriteLine(Move_Count);
        }
    }
}