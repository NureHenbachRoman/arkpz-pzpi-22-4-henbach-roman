using Battle_City.Fields;
using Battle_City.Internal_Code;
using Microsoft.VisualBasic.FileIO;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.CompilerServices;
using System.Text;
using System.Threading.Tasks;
using static Battle_City.Internal_Code.Globals;

namespace Battle_City.Game_Elements.Entities
{
    public abstract class Entity : Visible
    {
        public bool IsDead { get; private set; }
        protected EntitiesField entitiesField;

        public Entity(int x, int y, int width, int height, EntitiesField entitiesField) 
            : base(x, y, width, height)
        {
            this.entitiesField = entitiesField;
            this.entitiesField.PlaceOnField(this);
        }

        public virtual void Die()
        {
            IsDead = true;
            entitiesField.Remove(this);
        }
    }
}