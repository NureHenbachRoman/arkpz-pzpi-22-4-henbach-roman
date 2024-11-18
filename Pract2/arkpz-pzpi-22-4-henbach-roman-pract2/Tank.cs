using Battle_City.Fields;
using Battle_City.Internal_Code;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static Battle_City.Internal_Code.Globals;

namespace Battle_City.Game_Elements.Entities
{
    public abstract class Tank : MovingEntity
    {
        public Tank(int x, int y, Direction dir, Field field) : base(x, y, dir, TankWidth, TankHeight, field)
        {

            Speed = 1;
            IsMoving = false;
        }

        
        protected override void MoveHelper(Field field, int deltaX, int deltaY)
        {
            int xstart, ystart, xstop, ystop;
            (xstart, ystart, xstop, ystop) = (deltaX, deltaY) switch
            {
                (0, -1) => (X, Y - Speed, X + Width, Y),
                (0,  1) => (X, Y + Height, X + Width, Y + Height + Speed),
                (-1, 0) => (X - Speed, Y, X, Y + Height),
                (1,  0) => (X + Width, Y, X + Width + Speed, Y + Height),
                _ => throw new Exception("Wrong X or Y change value in MoveHelper method")
            };

            if (field.AreaIsAvailableForTank(xstart, ystart, xstop, ystop))
            {
                X += Speed * deltaX;
                Y += Speed * deltaY;
                IsMoving = true;
            }
        }
        
        public override void Move(Field field)
        {
            IsMoving = false;
            base.Move(field);
        }

        public void Shoot(Field field)
        {
            if (CountBulletsDeployedBy(this) > 0)
            {
                return;
            }
            (int bulX, int bulY) = Dir switch
            {
                Direction.Up => (X + 1, Y - BulletHeight),
                Direction.Down => (X + 1, Y + Height),
                Direction.Right => (X + Width, Y + 1),
                Direction.Left => (X - BulletWidth, Y + 1),
                _ => (0, 0)
            };
            if (field.AreaIsAvailableForBullet(bulX, bulY, bulX + BulletWidth, bulY + BulletHeight))
            {
                new Bullet(bulX, bulY, Dir, this, field);
            }
            else
            {
                (int xstart, int ystart, int xstop, int ystop) = Dir switch
                {
                    Direction.Up => (X, Y - 2, X + Width, Y),
                    Direction.Down => (X, Y + Height, X + Width, Y + Height + 2),
                    Direction.Right => (X + Width, Y, X + Width + 2, Y + Height),
                    Direction.Left => (X - 2, Y, X, Y + Height),
                    _ => (0, 0, 0, 0)
                };
                field.Destroy(xstart, ystart, xstop, ystop);
            }
        }
    }
}