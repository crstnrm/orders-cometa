export interface OrderRoundItem {
    name: string;
    quantity: number;
}

export interface OrderRound {
    created_at: Date;
    items: OrderRoundItem[];
}

export interface OrderItem {
    name: string;
    quantity: number;
    unit_price: number;
}

export interface Order {
    id: string;
    status: string;
    items: OrderItem[];
    rounds: OrderRound[];
    created_at: Date;
    is_paid: boolean;
    subtotal: number;
    discounts: number;
    total: number;
}