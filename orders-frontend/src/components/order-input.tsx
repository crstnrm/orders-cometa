'use client';

import { useState } from 'react';

interface Props {
  onSubmit: (orderId: string) => void;
}

export default function OrderInput({ onSubmit }: Props) {
  const [orderId, setOrderId] = useState('');

  const submitOrderId = (e: React.FormEvent) => {
    e.preventDefault();
    onSubmit(orderId);
  };

  return (
    <form onSubmit={submitOrderId} className="flex items-center space-x-4 max-w-md mx-auto mt-1 mb-6">
      <input
        type="text"
        value={orderId}
        onChange={(e) => setOrderId(e.target.value)}
        placeholder="Enter 1 or 2"
        className="flex-1 p-2 border text-gray-500 border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
      />
      <button
        type="submit"
        className="px-4 py-2 bg-blue-500 text-white rounded-lg shadow hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500"
      >
        Submit
      </button>
    </form>
  );
}
