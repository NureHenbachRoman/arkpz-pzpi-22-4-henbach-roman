using Battle_City.Fields;
using Battle_City.Internal_Code;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Battle_City.Game_Elements.Entities
{
    public class Enemy : Tank
    {
        private List<Direction> blockedDirections = new();
        public Enemy(int x, int y, Direction dir, Field field) : base(x, y, dir, field)
        {
            IsMoving = true;
        }

        public override void Move(Field field)
        {
            base.Move(field);

            Random rnd = new Random();
            List<Direction> availableDirections = new();

            if (IsMoving)
            {
                blockedDirections.Clear();
                return;
            }
            else
            {
                blockedDirections.Add(Dir);
                
                foreach (Direction direction in Enum.GetValues<Direction>())
                {
                    if (!blockedDirections.Contains(direction))
                    {
                        availableDirections.Add(direction);
                        IsMoving = true;
                    }
                }
                if (availableDirections.Count == 0)
                {
                    blockedDirections.Clear();
                    IsMoving = true;
                }
                else
                {
                    Dir = availableDirections[rnd.Next(availableDirections.Count)];
                }
            }                        
        }

        public void RandomShoot(Field field)
        {
            Random rnd = new Random();
            if (rnd.Next(100) < 5)
            {
                Shoot(field);
            }
        }
    }
}