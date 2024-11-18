using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Cryptography.X509Certificates;
using System.Text;
using System.Threading.Tasks;
using Battle_City.Game_Elements;
using Battle_City.Game_Elements.Cells;
using Battle_City.Internal_Code;
using Battle_City.Game_Elements.Entities;

namespace Battle_City.Fields
{
    public class Field : Visible
    {
        private Cell[,] _field;

        public Field(int width, int height, int x = 0, int y = 0) : base(x, y, width, height)
        {
            _field = new Cell[height, width];
        }

        public Cell this[int x, int y]
        {
            get
            {
                return _field[y, x];
            }
            set
            {
                _field[y, x] = value;
            }
        }
        public int Xmax { get { return _field.GetLength(1); } }
        public int Ymax { get { return _field.GetLength(0); } }

        public void Generate()
        {
            var _rnd = new Random();

            for (int i = 0; i < Xmax; i += 4)
            {
                for (int j = 0; j < Ymax; j += 4)
                {
                    Build.Block(this, i, j, Cell.cells[_rnd.Next(Cell.cells.Length)]);
                }
            }
            Build.Base(this);
        }


        public bool AreaIsAvailableForTank(int xstart, int ystart, int xstop, int ystop)
        {
            return AreaIsAvailableFor(xstart, ystart, xstop, ystop, (i, j) => !this[i, j].TanksCanMove);
        }

        public bool AreaIsAvailableForBullet(int xstart, int ystart, int xstop, int ystop)
        {
            return AreaIsAvailableFor(xstart, ystart, xstop, ystop, (i, j) => !this[i, j].BulletsCanMove);
        }

        private bool AreaIsAvailableFor(int xstart, int ystart, int xstop, int ystop, Func<int, int, bool> checker)
        {
            if (xstart < 0 || ystart < 0 || xstop > Xmax || ystop > Ymax)
            {
                return false;
            }

            for (int i = xstart; i < xstop; i++)
            {
                for (int j = ystart; j < ystop; j++)
                {
                    if (checker(i, j))
                    {
                        return false;
                    }
                }
            }
            return true;
        }

        public void Destroy(int xstart, int ystart, int xstop, int ystop)
        {
            for (int i = xstart; i < xstop; i++)
            {
                for (int j = ystart; j < ystop; j++)
                {
                    if (i < 0 || j < 0 || i >= Xmax || j >= Ymax)
                    {
                        continue;
                    }
                    if (this[i, j].IsDestroyable)
                    {
                        this[i, j] = new EmptyCell(i, j);
                        this[i, j].Draw();
                    }
                }
            }
        }

        public void Redraw(int xstart, int ystart, int xstop, int ystop)
        {
            for (int i = xstart; i <= xstop; i++)
            {
                for (int j = ystart; j <= ystop; j++)
                {
                    if (i >= 0 && j >= 0 && i < Xmax && j < Ymax)
                    {
                        this[i, j].Draw();
                    }
                }
            }
        }
    }
}