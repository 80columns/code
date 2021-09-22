/*
 * https://www.hackerrank.com/challenges/gena/problem
 */

using System;
using System.Collections.Generic;
using System.Linq;

namespace GenaPlayingHanoi {
    class HanoiGame {
        public List<sbyte>[] Posts;
        public HashSet<sbyte> Valid_Source_Post_Indices;
        public (sbyte Source, sbyte Destination) Previous_Move;
        public byte? Post_Zero_Top_Consecutive_Disk;
        private string Config_Str;
        private string Fuzzy_Config_Str;
        private byte Disk_Count;
        
        public HanoiGame(
            List<int> _Initial_Post_Config
        ) {
            this.Posts = new List<sbyte>[4] {
                new List<sbyte>(),
                new List<sbyte>(),
                new List<sbyte>(),
                new List<sbyte>()
            };
            this.Valid_Source_Post_Indices = new HashSet<sbyte>();
            this.Previous_Move = (-1, -1);
            this.Disk_Count = (byte)_Initial_Post_Config.Count;
            
            for (var i = (sbyte)(_Initial_Post_Config.Count - 1); i >= 0; i--) {
                this.Posts[_Initial_Post_Config[i] - 1].Add(i);
                this.Valid_Source_Post_Indices.Add((sbyte)(_Initial_Post_Config[i] - 1));
            }
            
            this.GenerateConfig();
            this.GenerateFuzzyConfig();
            this.FindPostZeroTopConsecutiveDisk();
        }
        
        public HanoiGame(
            int _Disk_Count
        ) {
            this.Posts = new List<sbyte>[4] {
                new List<sbyte>(),
                new List<sbyte>(),
                new List<sbyte>(),
                new List<sbyte>()
            };
            this.Valid_Source_Post_Indices = new HashSet<sbyte>() { 0 };
            this.Previous_Move = (-1, -1);
            this.Disk_Count = (byte)_Disk_Count;
            
            for (var i = (sbyte)(_Disk_Count - 1); i >= (0); i--) {
                this.Posts[0].Add(i);
            }
            
            this.GenerateConfig();
            this.GenerateFuzzyConfig();
            this.FindPostZeroTopConsecutiveDisk();
        }

        public HanoiGame(
            string _Config,
            (sbyte Source, sbyte Destination) _Previous_Move
        ) {
            this.Posts = new List<sbyte>[4] {
                new List<sbyte>(),
                new List<sbyte>(),
                new List<sbyte>(),
                new List<sbyte>()
            };
            this.Valid_Source_Post_Indices = new HashSet<sbyte>();
            this.Previous_Move = (
                _Previous_Move.Source,
                _Previous_Move.Destination
            );
            this.Disk_Count = 0;

            var Post_Index = (sbyte)3;

            for (var i = _Config.Length - 1; i >= 0; i--) {
                if (_Config[i] == '|') {
                    Post_Index--;
                } else {
                    this.Posts[Post_Index].Add(
                        (sbyte)(_Config[i] - 48)
                    );
                    this.Valid_Source_Post_Indices.Add(Post_Index);
                    this.Disk_Count++;
                }
            }
            
            this.GenerateConfig();
            this.GenerateFuzzyConfig();
            this.FindPostZeroTopConsecutiveDisk();
        }
        
        public override bool Equals(
            object _Other
        ) {
            return _Other is HanoiGame && this.Equals(_Other as HanoiGame);
        }
        
        public bool Equals(
            HanoiGame _Other
        ) {
            var Equal = true;
        
            for (var i = 0; i < 4; i++) {
                if (this.Posts[i].Count != _Other.Posts[i].Count) {
                    Equal = false;
                } else {
                    for (var j = 0; j < this.Posts[i].Count; j++) {
                        if (
                            this.Posts[i][(this.Posts[i].Count - 1) - j]
                         != _Other.Posts[i][(_Other.Posts[i].Count - 1) - j]
                        ) {
                            Equal = false;
                            break;
                        }
                    }
                }
                
                if (Equal == false) { break; }
            }
            
            return Equal;
        }
        
        public override int GetHashCode() {
            return this.Config_Str.GetHashCode();
        }

        public int GetFuzzyHashCode() {
            return this.Fuzzy_Config_Str.GetHashCode();
        }

        public string GetConfig() {
            return this.Config_Str;
        }

        public void MoveDisk(
            sbyte _Source_Post_Index,
            sbyte _Destination_Post_Index
        ) {
            this.Posts[_Destination_Post_Index].Add(
                this.Posts[_Source_Post_Index][this.Posts[_Source_Post_Index].Count - 1]
            );

            this.Posts[_Source_Post_Index].RemoveAt(this.Posts[_Source_Post_Index].Count - 1);

            this.Valid_Source_Post_Indices.Add(_Destination_Post_Index);

            if (this.Posts[_Source_Post_Index].Count == 0) {
                this.Valid_Source_Post_Indices.Remove(_Source_Post_Index);
            }

            this.GenerateConfig();
            this.GenerateFuzzyConfig();

            if (
                _Source_Post_Index == 0
             || _Destination_Post_Index == 0
            ) {
                this.FindPostZeroTopConsecutiveDisk();
            }
        }

        // compute the config string used for generating the object hashcode
        private void GenerateConfig() {
            var Config_Str_Index = 0;
            var Config_Str_Array = new char[this.Disk_Count + 3];
        
            for (var i = 0; i < 4; i++) {
                for (var j = 0; j < this.Posts[i].Count; j++) {
                    Config_Str_Array[Config_Str_Index++] =
                        (char)(this.Posts[i][(this.Posts[i].Count - 1) - j] + 48);
                }
                
                // add separator to specify post separation
                if (i < 3) {
                    Config_Str_Array[Config_Str_Index++] = '|';
                }
            }
        
            this.Config_Str = new String(Config_Str_Array);
        }

        private void GenerateFuzzyConfig() {
            var Fuzzy_Config_Str_Index = 0;
            var Fuzzy_Config_Str_Array = new char[this.Disk_Count + 3];

            // append the disks at post 0 first
            for (var i = 0; i < this.Posts[0].Count; i++) {
                Fuzzy_Config_Str_Array[Fuzzy_Config_Str_Index++] =
                    (char)(this.Posts[0][(this.Posts[0].Count - 1) - i] + 48);
            }

            Fuzzy_Config_Str_Array[Fuzzy_Config_Str_Index++] = '|';

            // sort the remaining 3 posts by the size of the top disk
            // in smallest to largest order, with empty posts occuring first
            var Top_Disk_Index_Map = new Dictionary<int, int>();
            var Empty_Post_Count = 0;

            for (var i = 1; i < 4; i++) {
                if (this.Posts[i].Count > 0) {
                    Top_Disk_Index_Map[this.Posts[i][this.Posts[i].Count - 1]] = i;
                } else {
                    Empty_Post_Count++;
                }
            }

            var Ordered_Top_Disks = Top_Disk_Index_Map.Keys.ToList();
            Ordered_Top_Disks.Sort();

            for (var i = 0; i < Empty_Post_Count - 1; i++) {
                Fuzzy_Config_Str_Array[Fuzzy_Config_Str_Index++] = '|';
            }

            for (var i = 0; i < Ordered_Top_Disks.Count; i++) {
                var Post_Index = Top_Disk_Index_Map[Ordered_Top_Disks[i]];

                for (var j = 0; j < this.Posts[Post_Index].Count; j++) {
                    Fuzzy_Config_Str_Array[Fuzzy_Config_Str_Index++] = 
                        (char)(this.Posts[Post_Index][(this.Posts[Post_Index].Count - 1) - j] + 48);
                }

                if (i < Ordered_Top_Disks.Count - 1) {
                    Fuzzy_Config_Str_Array[Fuzzy_Config_Str_Index++] = '|';
                }
            }

            this.Fuzzy_Config_Str = new String(Fuzzy_Config_Str_Array);
        }
        
        private void FindPostZeroTopConsecutiveDisk() {
            if (this.Posts[0].Count == 0) {
                this.Post_Zero_Top_Consecutive_Disk = null;
            } else if (
                this.Posts[0].Count == 1
             && this.Posts[0][this.Posts[0].Count - 1] == this.Disk_Count - 1
            ) {
                this.Post_Zero_Top_Consecutive_Disk = (byte)(this.Disk_Count - 1);
            } else {
                var Top_Consecutive_Disk = this.Disk_Count;

                for (var j = this.Posts[0].Count - 1; j >= 0; j--) {
                    if (this.Posts[0][(this.Posts[0].Count - 1) - j] == Top_Consecutive_Disk - 1) {
                        Top_Consecutive_Disk--;
                    } else {
                        break;
                    }
                }

                this.Post_Zero_Top_Consecutive_Disk =
                    (Top_Consecutive_Disk == this.Disk_Count) ?
                        null as byte? : Top_Consecutive_Disk;
            }
        }
    }

    class Program {
        static int GetMinimumMoves(
            List<int> _Initial_Post_Config
        ) {
            var Other_Post_Indices = new Dictionary<sbyte, HashSet<sbyte>>() {
                [0] = new HashSet<sbyte>() { 1, 2, 3},
                [1] = new HashSet<sbyte>() { 0, 2, 3},
                [2] = new HashSet<sbyte>() { 0, 1, 3},
                [3] = new HashSet<sbyte>() { 0, 1, 2}
            };

            var Initial_Game = new HanoiGame(_Initial_Post_Config);
            var Final_Game = new HanoiGame(_Initial_Post_Config.Count);
            
            var Current_Games = new HashSet<HanoiGame>() { Initial_Game };
            var Previous_Game_Indices = new HashSet<int>();
            var Next_Games = new HashSet<HanoiGame>();
            
            var Search_Level = 1;
            var Post_Zero_Search_Disk = _Initial_Post_Config.Count - 1;
            var Post_Zero_Minimum_Height = 0;
            var Post_Zero_Required_Top_Disk_Size = -1;
            
            while (true) {
                foreach (var Current_Game in Current_Games) {
                    // iterate over each post, checking where the top disk
                    // can be moved
                    foreach (var Source_Post_Index in Current_Game.Valid_Source_Post_Indices) {
                        // check each of the other posts in the game
                        // to see if the top disk can be moved there
                        foreach (
                            var Destination_Post_Index
                                in Other_Post_Indices[Source_Post_Index]
                        ) {
                            // check if the top disk at Source_Post_Index
                            // can be moved to Destination_Post_Index
                            if (
                                // the destination post must either be
                                // (1) empty, or (2) have a top disk that is
                                // larger than the top disk on the current post
                                (
                                    Current_Game.Posts[Destination_Post_Index].Count == 0
                                 || (
                                        Current_Game.Posts[Source_Post_Index].Count > 0
                                     && Current_Game.Posts[Source_Post_Index][Current_Game.Posts[Source_Post_Index].Count - 1] < Current_Game.Posts[Destination_Post_Index][Current_Game.Posts[Destination_Post_Index].Count - 1]
                                    )
                                )
                                // avoid processing the "undo" of the prior move
                                // that produced this game configuration
                             && (
                                    Current_Game.Previous_Move.Source != Destination_Post_Index
                                 || Current_Game.Previous_Move.Destination != Source_Post_Index
                                )
                            ) {
                                // temporarily make the move on this object
                                var Temp_Game = new HanoiGame(
                                    Current_Game.GetConfig(),
                                    (Source_Post_Index, Destination_Post_Index)
                                );
                                Temp_Game.MoveDisk(
                                    Source_Post_Index,
                                    Destination_Post_Index
                                );
                                var Temp_Game_Fuzzy_Index = Temp_Game.GetFuzzyHashCode();
                                
                                if (
                                    Temp_Game.Posts[0].Count == Post_Zero_Minimum_Height + 1
                                 && Temp_Game.Posts[0][Temp_Game.Posts[0].Count - 1] == Post_Zero_Search_Disk
                                ) {
                                    var Post_Zero_Matches = true;
                                    var Temp_Post_Zero_Disk = Post_Zero_Search_Disk;
                                    
                                    for (var i = 0; i < Post_Zero_Minimum_Height; i++) {
                                        if (Temp_Game.Posts[0][(Temp_Game.Posts[0].Count - 1) - i] != Temp_Post_Zero_Disk) {
                                            Post_Zero_Matches = false;
                                            break;
                                        }
                                        
                                        Temp_Post_Zero_Disk++;
                                    }
                                    
                                    if (Post_Zero_Matches) {
                                        Post_Zero_Required_Top_Disk_Size = Post_Zero_Search_Disk;
                                        Post_Zero_Minimum_Height++;
                                        Post_Zero_Search_Disk--;

                                        if (Post_Zero_Required_Top_Disk_Size < _Initial_Post_Config.Count - 2) {
                                            Next_Games.RemoveWhere(
                                                game => game.Post_Zero_Top_Consecutive_Disk.HasValue == false
                                                     || (
                                                            (
                                                                game.Posts[0].Count < Post_Zero_Minimum_Height - 2
                                                             || game.Post_Zero_Top_Consecutive_Disk.Value != Post_Zero_Required_Top_Disk_Size + 2
                                                            )
                                                         && (
                                                                game.Posts[0].Count < Post_Zero_Minimum_Height - 1
                                                             || game.Post_Zero_Top_Consecutive_Disk.Value != Post_Zero_Required_Top_Disk_Size + 1
                                                            )
                                                         && (
                                                                game.Posts[0].Count < Post_Zero_Minimum_Height
                                                             || game.Post_Zero_Top_Consecutive_Disk.Value != Post_Zero_Required_Top_Disk_Size
                                                            )
                                                        )
                                            );
                                        }
                                    }
                                }
                                
                                if (
                                    (
                                        Search_Level == 0
                                     || Previous_Game_Indices.Contains(Temp_Game_Fuzzy_Index) == false
                                    )
                                 && (
                                        (
                                            Post_Zero_Required_Top_Disk_Size == -1
                                         || Post_Zero_Required_Top_Disk_Size == _Initial_Post_Config.Count - 1
                                         || Post_Zero_Required_Top_Disk_Size == _Initial_Post_Config.Count - 2
                                        )
                                     || (
                                            Temp_Game.Post_Zero_Top_Consecutive_Disk.HasValue
                                         && (
                                                (
                                                    Temp_Game.Posts[0].Count >= Post_Zero_Minimum_Height - 2
                                                 && Temp_Game.Post_Zero_Top_Consecutive_Disk.Value == Post_Zero_Required_Top_Disk_Size + 2
                                                )
                                             || (
                                                    Temp_Game.Posts[0].Count >= Post_Zero_Minimum_Height - 1
                                                 && Temp_Game.Post_Zero_Top_Consecutive_Disk.Value == Post_Zero_Required_Top_Disk_Size + 1
                                                )
                                             || (
                                                    Temp_Game.Posts[0].Count >= Post_Zero_Minimum_Height
                                                 && Temp_Game.Post_Zero_Top_Consecutive_Disk.Value == Post_Zero_Required_Top_Disk_Size
                                                )
                                            )
                                        )
                                    )
                                ) {
                                    Next_Games.Add(Temp_Game);
                                    Previous_Game_Indices.Add(Temp_Game_Fuzzy_Index);
                                }
                            }
                        }
                    }
                }

                // at the end of each loop, check whether the group of next
                // games to process contains the final game configuration
                if (Next_Games.Contains(Final_Game)) {
                    break;
                }

                Current_Games.Clear();
                Current_Games.UnionWith(Next_Games);
                Next_Games.Clear();

                Search_Level++;
            }
            
            return Search_Level;
        }

        static void Main(string[] args) {
            // expected output is 42
            Console.WriteLine(GetMinimumMoves(
                new List<int>() { 4, 2, 2, 3, 2, 1, 4, 1, 3, 4 }
            ));
        }
    }
}