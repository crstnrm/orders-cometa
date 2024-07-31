orders = [
    {
        "id": "1",
        "created_at": "2024-09-10 12:00:00",
        "status": "OPENED",
        "discount": {"value": 10, "type": "PERCENTAGE"},
        "items": [
            {"name": "Corona", "unit_price": 10_000, "quantity": 3},
            {"name": "Club Colombia", "unit_price": 11_900, "quantity": 2},
            {"name": "Quilmes", "unit_price": 8_900, "quantity": 2},
        ],
        "rounds": [
            {
                "created_at": "2024-09-10 12:00:30",
                "items": [
                    {"name": "Corona", "quantity": 3},
                    {"name": "Club Colombia", "quantity": 1},
                ],
            },
            {
                "created_at": "2024-09-10 12:20:31",
                "items": [
                    {"name": "Club Colombia", "quantity": 1},
                    {"name": "Quilmes", "quantity": 2},
                ],
            },
            {
                "created_at": "2024-09-10 12:43:21",
                "items": [{"name": "Quilmes", "quantity": 3}],
            },
        ],
    },
    {
        "id": "2",
        "created_at": "2024-09-10 12:00:00",
        "status": "OPENED",
        "discount": {"value": 50_000, "type": "AMOUNT"},
        "items": [
            {
                "name": "Corona",
                "unit_price": 11_000,
                "quantity": 10,
            },
            {
                "name": "Club Colombia",
                "unit_price": 13_900,
                "quantity": 16,
            },
            {
                "name": "Quilmes",
                "unit_price": 10_900,
                "quantity": 5,
            },
        ],
        "rounds": [
            {
                "created_at": "2024-09-10 12:00:30",
                "items": [
                    {"name": "Corona", "quantity": 10},
                    {"name": "Club Colombia", "quantity": 8},
                ],
            },
            {
                "created_at": "2024-09-10 12:20:31",
                "items": [
                    {"name": "Club Colombia", "quantity": 8},
                    {"name": "Quilmes", "quantity": 2},
                ],
            },
            {
                "created_at": "2024-09-10 12:43:21",
                "items": [{"name": "Quilmes", "quantity": 3}],
            },
        ],
    },
]
