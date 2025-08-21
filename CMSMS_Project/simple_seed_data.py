#!/usr/bin/env python
"""
Simple Sample Data Seeding Script for Cosmetic Manufacturing System
This script populates the database with basic test data
"""

import os
import sys
import django
from datetime import datetime as dt, timedelta

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Cosmetics_Manufacturing_And_Sales_Management_System.settings')
django.setup()

from django.contrib.auth.models import User, Group
from FormulationAndLabManagement.models import *
from BatchProductionManagement.models import *

def create_groups():
    """Create user groups for different roles"""
    print("Creating user groups...")
    
    groups = [
        'LaboratoryManager',
        'BatchProductionManager', 
        'SupplierManager',
        'WarehouseManager',
        'SalesManager',
        'EmployeeManager',
        'CostAnalysisManager',
        'DeliveryManager',
        'customer'
    ]
    
    created_groups = {}
    for group_name in groups:
        group, created = Group.objects.get_or_create(name=group_name)
        if created:
            print(f"✓ Created group: {group_name}")
        else:
            print(f"✓ Group already exists: {group_name}")
        created_groups[group_name] = group
    
    return created_groups

def create_superuser():
    """Create a superuser account"""
    print("\nCreating superuser...")
    
    if not User.objects.filter(username='admin').exists():
        user = User.objects.create_superuser(
            username='admin',
            email='admin@glamourcosmetics.com',
            password='Admin123!'
        )
        print("✓ Created superuser: admin / Admin123!")
    else:
        print("✓ Superuser already exists: admin")
    
    return User.objects.get(username='admin')

def create_sample_products():
    """Create sample cosmetic products"""
    print("\nCreating sample products...")
    
    products_data = [
        {
            'product_name': 'Glow Radiance Serum',
            'product_category': 'Skin Cosmetics',
            'description': 'Advanced anti-aging serum with vitamin C and hyaluronic acid',
            'preparation_method': 'Mix vitamin C powder with hyaluronic acid solution, add preservatives and stabilizers',
            'duration': timedelta(days=365)
        },
        {
            'product_name': 'Silk Smooth Hair Mask',
            'product_category': 'Hair Cosmetics',
            'description': 'Deep conditioning hair mask with argan oil and keratin',
            'preparation_method': 'Blend argan oil with keratin proteins, add conditioning agents and fragrance',
            'duration': timedelta(days=730)
        },
        {
            'product_name': 'Perfect Nail Polish',
            'product_category': 'Nail Cosmetics',
            'description': 'Long-lasting nail polish with chip-resistant formula',
            'preparation_method': 'Mix nitrocellulose with plasticizers, add pigments and solvents',
            'duration': timedelta(days=1095)
        },
        {
            'product_name': 'Natural Foundation',
            'product_category': 'Face Makeup',
            'description': 'Mineral-based foundation with SPF protection',
            'preparation_method': 'Blend mineral pigments with zinc oxide, add natural oils and preservatives',
            'duration': timedelta(days=730)
        },
        {
            'product_name': 'Hydrating Face Cream',
            'product_category': 'Skin Cosmetics',
            'description': 'Moisturizing cream with ceramides and niacinamide',
            'preparation_method': 'Emulsify water and oil phases, add active ingredients and stabilizers',
            'duration': timedelta(days=730)
        }
    ]
    
    created_products = []
    for data in products_data:
        product, created = products.objects.get_or_create(
            product_name=data['product_name'],
            defaults=data
        )
        if created:
            print(f"✓ Created product: {product.product_name}")
        else:
            print(f"✓ Product already exists: {product.product_name}")
        created_products.append(product)
    
    return created_products

def create_sample_formulations(products):
    """Create sample formulations for products"""
    print("\nCreating sample formulations...")
    
    formulations_data = [
        {
            'product': products[0],  # Glow Radiance Serum
            'raw_materials': [
                ('Vitamin C Powder', 5.0),
                ('Hyaluronic Acid', 2.0),
                ('Distilled Water', 70.0),
                ('Preservative', 1.0),
                ('Stabilizer', 0.5)
            ]
        },
        {
            'product': products[1],  # Silk Smooth Hair Mask
            'raw_materials': [
                ('Argan Oil', 15.0),
                ('Keratin Protein', 8.0),
                ('Conditioning Agent', 5.0),
                ('Fragrance', 2.0),
                ('Preservative', 1.0)
            ]
        },
        {
            'product': products[2],  # Perfect Nail Polish
            'raw_materials': [
                ('Nitrocellulose', 20.0),
                ('Plasticizer', 15.0),
                ('Pigment', 8.0),
                ('Solvent', 55.0),
                ('Stabilizer', 2.0)
            ]
        }
    ]
    
    for data in formulations_data:
        product = data['product']
        for material_name, quantity in data['raw_materials']:
            formulation_obj, created = formulation.objects.get_or_create(
                product_name=product,
                raw_material=material_name,
                defaults={'formulation_qty': quantity}
            )
            if created:
                print(f"✓ Created formulation: {material_name} for {product.product_name}")
            else:
                print(f"✓ Formulation already exists: {material_name} for {product.product_name}")

def create_sample_equipment():
    """Create sample laboratory equipment"""
    print("\nCreating sample equipment...")
    
    equipment_data = [
        {'equipment_id': 'EQ001', 'category': 'Test Tube', 'condition': 'Brand New'},
        {'equipment_id': 'EQ002', 'category': 'Flask', 'condition': 'Used'},
        {'equipment_id': 'EQ003', 'category': 'Beaker', 'condition': 'Brand New'},
        {'equipment_id': 'EQ004', 'category': 'Pipette', 'condition': 'Used'},
        {'equipment_id': 'EQ005', 'category': 'Burette', 'condition': 'Need Repair'},
        {'equipment_id': 'EQ006', 'category': 'Measuring Cylinder', 'condition': 'Brand New'},
        {'equipment_id': 'EQ007', 'category': 'Laboratory Stand', 'condition': 'Used'},
        {'equipment_id': 'EQ008', 'category': 'Funnel', 'condition': 'Brand New'}
    ]
    
    for data in equipment_data:
        equipment, created = equipments.objects.get_or_create(
            equipment_id=data['equipment_id'],
            defaults=data
        )
        if created:
            print(f"✓ Created equipment: {equipment.equipment_id} - {equipment.category}")
        else:
            print(f"✓ Equipment already exists: {equipment.equipment_id}")

def create_sample_chemicals():
    """Create sample test chemicals"""
    print("\nCreating sample chemicals...")
    
    chemicals_data = [
        {'chemical_name': 'Sodium Hydroxide', 'available_quantity': 500.0, 'status': 'Available'},
        {'chemical_name': 'Hydrochloric Acid', 'available_quantity': 300.0, 'status': 'Available'},
        {'chemical_name': 'Ethanol', 'available_quantity': 1000.0, 'status': 'Available'},
        {'chemical_name': 'Distilled Water', 'available_quantity': 5000.0, 'status': 'Available'},
        {'chemical_name': 'Phenolphthalein', 'available_quantity': 50.0, 'status': 'Available'},
        {'chemical_name': 'Methyl Orange', 'available_quantity': 25.0, 'status': 'Not Available'}
    ]
    
    for data in chemicals_data:
        chemical, created = test_chemicals.objects.get_or_create(
            chemical_name=data['chemical_name'],
            defaults=data
        )
        if created:
            print(f"✓ Created chemical: {chemical.chemical_name}")
        else:
            print(f"✓ Chemical already exists: {chemical.chemical_name}")

def create_sample_tests(products):
    """Create sample laboratory tests"""
    print("\nCreating sample tests...")
    
    tests_data = [
        {
            'product': products[0],
            'test_name': 'pH Stability Test',
            'method': 'Measure pH at 25°C, 40°C, and 50°C over 3 months',
            'status': 'Pending'
        },
        {
            'product': products[1],
            'test_name': 'Viscosity Test',
            'method': 'Measure viscosity using Brookfield viscometer at 25°C',
            'status': 'Success'
        },
        {
            'product': products[2],
            'test_name': 'Drying Time Test',
            'method': 'Apply polish and measure time to complete dryness',
            'status': 'Pending'
        }
    ]
    
    for data in tests_data:
        test, created = schedule_test.objects.get_or_create(
            test_name=data['test_name'],
            defaults=data
        )
        if created:
            print(f"✓ Created test: {test.test_name}")
        else:
            print(f"✓ Test already exists: {test.test_name}")

def create_sample_raw_materials():
    """Create sample raw materials for batch production"""
    print("\nCreating sample raw materials...")
    
    materials_data = [
        {'name': 'Vitamin C Powder', 'quantity': 1000.0, 'reorder_level': 200.0},
        {'name': 'Hyaluronic Acid', 'quantity': 500.0, 'reorder_level': 100.0},
        {'name': 'Argan Oil', 'quantity': 800.0, 'reorder_level': 150.0},
        {'name': 'Keratin Protein', 'quantity': 600.0, 'reorder_level': 120.0},
        {'name': 'Nitrocellulose', 'quantity': 1200.0, 'reorder_level': 250.0},
        {'name': 'Distilled Water', 'quantity': 5000.0, 'reorder_level': 1000.0}
    ]
    
    for data in materials_data:
        material, created = RawMaterial.objects.get_or_create(
            name=data['name'],
            defaults=data
        )
        if created:
            print(f"✓ Created raw material: {material.name}")
        else:
            print(f"✓ Raw material already exists: {material.name}")

def create_sample_productions(products):
    """Create sample production schedules"""
    print("\nCreating sample production schedules...")
    
    productions_data = [
        {
            'product_code': products[0],
            'target_quantity': 1000,
            'net_weight': 30,
            'due_date': dt.now().date() + timedelta(days=7),
            'status': 'Scheduled'
        },
        {
            'product_code': products[1],
            'target_quantity': 500,
            'net_weight': 200,
            'due_date': dt.now().date() + timedelta(days=14),
            'status': 'On Hold'
        },
        {
            'product_code': products[2],
            'target_quantity': 2000,
            'net_weight': 15,
            'due_date': dt.now().date() + timedelta(days=21),
            'status': 'Scheduled'
        }
    ]
    
    created_productions = []
    for data in productions_data:
        production, created = ScheduleProduction.objects.get_or_create(
            product_code=data['product_code'],
            due_date=data['due_date'],
            defaults=data
        )
        if created:
            print(f"✓ Created production schedule: {production.product_code.product_name}")
        else:
            print(f"✓ Production schedule already exists: {production.product_code.product_name}")
        created_productions.append(production)
    
    return created_productions

def create_sample_machinery():
    """Create sample production machinery"""
    print("\nCreating sample machinery...")
    
    machinery_data = [
        {
            'item_name': 'Mixing Tank 1000L',
            'model': 'MT-1000',
            'year': 2022,
            'description': 'Large capacity mixing tank for cosmetic production',
            'power_consumption': 5.5,
            'net_weight': 800.0,
            'dimensions': '2000x1500x1800',
            'date_purchased': dt.now().date() - timedelta(days=365),
            'repair_duration': 30,
            'condition': 'Brand New'
        },
        {
            'item_name': 'Tube Filler',
            'model': 'TF-200',
            'year': 2021,
            'description': 'Automatic tube filling machine',
            'power_consumption': 3.2,
            'net_weight': 450.0,
            'dimensions': '1500x800x1200',
            'date_purchased': dt.now().date() - timedelta(days=730),
            'repair_duration': 45,
            'condition': 'Used'
        },
        {
            'item_name': 'Bottle Capper',
            'model': 'BC-150',
            'year': 2023,
            'description': 'Automatic bottle capping machine',
            'power_consumption': 2.8,
            'net_weight': 300.0,
            'dimensions': '1200x600x1000',
            'date_purchased': dt.now().date() - timedelta(days=180),
            'repair_duration': 30,
            'condition': 'Brand New'
        }
    ]
    
    for data in machinery_data:
        machine, created = Machine.objects.get_or_create(
            item_name=data['item_name'],
            defaults=data
        )
        if created:
            print(f"✓ Created machinery: {machine.item_name}")
        else:
            print(f"✓ Machinery already exists: {machine.item_name}")

def create_sample_users(groups):
    """Create sample users for different roles"""
    print("\nCreating sample users...")
    
    users_data = [
        {
            'username': 'lab_manager',
            'email': 'lab@glamourcosmetics.com',
            'password': 'Lab123!',
            'first_name': 'Dr. Sarah',
            'last_name': 'Johnson',
            'groups': ['LaboratoryManager']
        },
        {
            'username': 'production_manager',
            'email': 'production@glamourcosmetics.com',
            'password': 'Prod123!',
            'first_name': 'Mike',
            'last_name': 'Chen',
            'groups': ['BatchProductionManager']
        },
        {
            'username': 'warehouse_manager',
            'email': 'warehouse@glamourcosmetics.com',
            'password': 'Ware123!',
            'first_name': 'Lisa',
            'last_name': 'Rodriguez',
            'groups': ['WarehouseManager']
        },
        {
            'username': 'sales_manager',
            'email': 'sales@glamourcosmetics.com',
            'password': 'Sales123!',
            'first_name': 'David',
            'last_name': 'Thompson',
            'groups': ['SalesManager']
        }
    ]
    
    for data in users_data:
        if not User.objects.filter(username=data['username']).exists():
            user = User.objects.create_user(
                username=data['username'],
                email=data['email'],
                password=data['password'],
                first_name=data['first_name'],
                last_name=data['last_name']
            )
            
            # Add user to groups
            for group_name in data['groups']:
                if group_name in groups:
                    user.groups.add(groups[group_name])
            
            print(f"✓ Created user: {user.username} / {data['password']}")
        else:
            print(f"✓ User already exists: {data['username']}")

def main():
    """Main function to run all data seeding"""
    print("🌟 Starting Data Seeding for Cosmetic Manufacturing System")
    print("=" * 60)
    
    try:
        # Create groups and superuser
        groups = create_groups()
        admin_user = create_superuser()
        
        # Create sample data
        products = create_sample_products()
        create_sample_formulations(products)
        create_sample_equipment()
        create_sample_chemicals()
        create_sample_tests(products)
        create_sample_raw_materials()
        productions = create_sample_productions(products)
        create_sample_machinery()
        create_sample_users(groups)
        
        print("\n" + "=" * 60)
        print("🎉 Data Seeding Completed Successfully!")
        print("=" * 60)
        print("\n📋 Sample Data Created:")
        print(f"  • Products: {len(products)}")
        print(f"  • Equipment: {equipments.objects.count()}")
        print(f"  • Chemicals: {test_chemicals.objects.count()}")
        print(f"  • Raw Materials: {RawMaterial.objects.count()}")
        print(f"  • Production Schedules: {ScheduleProduction.objects.count()}")
        print(f"  • Machinery: {Machine.objects.count()}")
        print(f"  • Users: {User.objects.count()}")
        
        print("\n🔑 Login Credentials:")
        print("  • Admin: admin / Admin123!")
        print("  • Lab Manager: lab_manager / Lab123!")
        print("  • Production Manager: production_manager / Prod123!")
        print("  • Warehouse Manager: warehouse_manager / Ware123!")
        print("  • Sales Manager: sales_manager / Sales123!")
        
        print("\n🌐 Access your system at: http://127.0.0.1:8000/")
        print("📊 Admin panel: http://127.0.0.1:8000/admin/")
        
    except Exception as e:
        print(f"\n❌ Error during data seeding: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    main()
