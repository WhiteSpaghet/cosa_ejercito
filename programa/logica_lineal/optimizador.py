from datos.datos_unidades import UNITS, RESOURCES

def optimize_army():
    best_power = 0
    best_config = {'swordsmen': 0, 'bowmen': 0, 'horsemen': 0}

    # Rango razonable de búsqueda
    for s in range(0, 21):
        for b in range(0, 21):
            for h in range(0, 21):
                food = s * UNITS['swordsmen']['food'] + b * UNITS['bowmen']['food'] + h * UNITS['horsemen']['food']
                wood = s * UNITS['swordsmen']['wood'] + b * UNITS['bowmen']['wood']
                gold = b * UNITS['bowmen']['gold'] + h * UNITS['horsemen']['gold']

                if food <= RESOURCES['food'] and wood <= RESOURCES['wood'] and gold <= RESOURCES['gold']:
                    power = s * UNITS['swordsmen']['power'] + b * UNITS['bowmen']['power'] + h * UNITS['horsemen']['power']
                    if power > best_power:
                        best_power = power
                        best_config = {'swordsmen': s, 'bowmen': b, 'horsemen': h}

    best_config['total_power'] = best_power
    return best_config