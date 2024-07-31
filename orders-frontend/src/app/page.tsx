import { getOrderById } from "@/components/order-actions";
import OrderSection from "@/components/order-section";


export default function Home() {
  return (
    <main className="font-poppins mx-10">
      <div className="flex items-center max-w-md mx-auto mt-6">
        <h1 className="text-2xl font-bold mb-4">Orders</h1>
      </div>
      <OrderSection getOrderById={getOrderById} />
    </main>
  );
}