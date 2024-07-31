'use client';

import { useState } from 'react';
import { Order } from '@/app/types';
import OrderInput from './order-input';
import OrderDetail from './order-detail';

interface Props {
  getOrderById: (id: string) => Promise<Order>;
}

export default function OrderSection({ getOrderById }: Props) {
  const [order, setOrder] = useState<Order | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const submitOrderId = async (orderId: string) => {
    setIsLoading(true);
    setError(null);
    try {
      setOrder(await getOrderById(orderId));
    } catch (err) {
      setError((err as Error).message);
      setOrder(null);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <>
      <OrderInput onSubmit={submitOrderId} />
      {isLoading && <p>Loading...</p>}
      {error && <p className="text-red-500">Error: {error}</p>}
      {order && <OrderDetail order={order} />}
    </>
  );
}