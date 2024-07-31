import { Order } from "@/app/types";

interface Props {
  order: Order;
}

export default function OrderDetail({ order }: Props) {
  return (
    <div className="max-w-3xl mx-auto m-4 p-6 bg-gray-50 rounded-lg shadow-md dark:bg-gray-900">
      <div className="flex items-center justify-between border-b border-gray-200 dark:border-gray-700 mb-4 pb-2">
        <h1 className="text-2xl font-bold text-gray-900 dark:text-white">Order Details # {order.id} ({order.status})</h1>
        <p className="text-sm text-gray-600 dark:text-gray-400">Created at {order.created_at + ""}</p>
      </div>

      <div className="mb-6">
        <h2 className="text-xl font-bold text-gray-800 dark:text-gray-200">Summary</h2>
        <div className="flex justify-between">
          <p className="text-md">Subtotal:</p>
          <p className="text-md">${order.subtotal}</p>
        </div>
        <div className="flex justify-between">
          <p className="text-md">Discounts:</p>
          <p className="text-md">-${order.discounts}</p>
        </div>
        <div className="flex justify-between">
          <p className="text-md font-semibold">Total:</p>
          <p className="text-md font-semibold">${order.total}</p>
        </div>
      </div>

      <div className="mb-6">
        <h2 className="text-xl font-bold text-gray-800 dark:text-gray-200 mb-2">Items Summary</h2>
        <div>
          {order.items.map((item, index) => (
            <div key={index} className="flex mb-1 justify-between">
              <p className="flex items-center text-md">
                <img className="w-8 h-8 rounded-lg mr-2" src="beer.jpg" alt="Item image" />
                <strong>{item.quantity}</strong> x {item.name} <span className="ms-1 text-sm text-gray-500">(${item.unit_price})</span>
              </p>
              <p className="text-md">${item.unit_price * item.quantity}</p>
            </div>
          ))}
        </div>
      </div>

      <div className="mb-6">
        <h2 className="text-xl mb-2 font-bold text-gray-800 dark:text-gray-200">Rounds</h2>
        <div className="grid grid-cols-1 gap-4">
          {order.rounds.map((round, roundIndex) => (
            <div key={roundIndex} className="bg-white border border-gray-200 rounded-lg shadow-md p-4 dark:border-gray-700 dark:bg-gray-800">
              <div className="flex items-center justify-between border-b border-gray-200 dark:border-gray-700 mb-4 pb-2">
                <h1 className="text-md text-gray-900 dark:text-white">Round {roundIndex + 1}</h1>
                <p className="text-sm text-gray-600 dark:text-gray-400">Created at {round.created_at + ""}</p>
              </div>
              <ul className="ml-4 list-none text-sm text-gray-700 dark:text-gray-400">
                {round.items.map((item, itemIndex) => (
                  <li key={itemIndex} className="mb-1">
                    <strong>{item.quantity}</strong> {item.name}
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
