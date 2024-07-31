'use server';

import { Order } from "@/app/types";

export async function getOrderById(id: string): Promise<Order> {
  const response = await fetch(`http://api:8000/orders/${id}`);

  const responseData = await response.json();

  if (response.status === 400) {
    // Handle 400 Bad Request
    throw new Error(responseData.message || 'Bad request: Invalid order ID');
  }

  if (!response.ok) {
    // Handle other error statuses
    throw new Error(responseData.message || `Failed to fetch data: ${response.statusText}`);
  }

  return responseData as Order;
}