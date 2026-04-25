"use client"
import { motion } from "framer-motion";
import { Search, Star } from "lucide-react";

export default function Page() {
  return (
    <div className="bg-gray-50 text-gray-900">
      {/* HERO SECTION */}
      <section className="relative h-screen flex items-center justify-center overflow-hidden">
        <img
          src="https://images.unsplash.com/photo-1507525428034-b723cf961d3e"
          className="absolute inset-0 w-full h-full object-cover"
          alt="hero"
        />
        <div className="absolute inset-0 bg-black/50"></div>

        <motion.div
          initial={{ opacity: 0, y: 50 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 1 }}
          className="relative text-center text-white px-4"
        >
          <h1 className="text-5xl md:text-7xl font-bold mb-6">
            Find your next stay
          </h1>
          <p className="text-lg md:text-xl mb-8">
            Discover unique places to stay anywhere in the world
          </p>

          <div className="bg-white rounded-full flex items-center p-2 max-w-xl mx-auto shadow-lg">
            <input
              className="flex-1 px-4 py-2 outline-none text-black"
              placeholder="Where are you going?"
            />
            <button className="bg-pink-500 text-white p-3 rounded-full">
              <Search />
            </button>
          </div>
        </motion.div>
      </section>

      {/* FEATURES */}
      <section className="py-20 px-6 max-w-7xl mx-auto">
        <h2 className="text-4xl font-bold mb-12 text-center">
          Explore Nearby
        </h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          {[1, 2, 3].map((item) => (
            <motion.div
              key={item}
              whileHover={{ scale: 1.05 }}
              className="bg-white rounded-2xl shadow-lg overflow-hidden"
            >
              <img
                src={`https://source.unsplash.com/random/400x300?sig=${item}`}
                className="w-full h-56 object-cover"
              />
              <div className="p-4">
                <h3 className="text-xl font-semibold">Beautiful Location</h3>
                <p className="text-gray-600">Stay in amazing places</p>
              </div>
            </motion.div>
          ))}
        </div>
      </section>

      {/* EXPERIENCE SECTION */}
      <section className="bg-black text-white py-20 px-6">
        <div className="max-w-7xl mx-auto grid md:grid-cols-2 gap-10 items-center">
          <motion.div
            initial={{ x: -100, opacity: 0 }}
            whileInView={{ x: 0, opacity: 1 }}
            transition={{ duration: 1 }}
          >
            <h2 className="text-4xl font-bold mb-6">
              Unique Experiences
            </h2>
            <p className="text-gray-300">
              Join activities led by local hosts and explore the culture deeply.
            </p>
          </motion.div>

          <motion.img
            src="https://images.unsplash.com/photo-1526772662000-3f88f10405ff"
            className="rounded-2xl shadow-xl"
            initial={{ x: 100, opacity: 0 }}
            whileInView={{ x: 0, opacity: 1 }}
            transition={{ duration: 1 }}
          />
        </div>
      </section>

      {/* LISTINGS */}
      <section className="py-20 px-6 max-w-7xl mx-auto">
        <h2 className="text-4xl font-bold mb-12 text-center">
          Featured Stays
        </h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          {[1, 2, 3].map((item) => (
            <motion.div
              key={item}
              whileHover={{ y: -10 }}
              className="bg-white rounded-2xl shadow-lg overflow-hidden"
            >
              <img
                src={`https://source.unsplash.com/random/400x300?house=${item}`}
                className="w-full h-56 object-cover"
              />
              <div className="p-4">
                <h3 className="text-lg font-semibold">Luxury Apartment</h3>
                <div className="flex items-center text-yellow-500">
                  <Star size={16} />
                  <span className="ml-1 text-gray-700">4.8</span>
                </div>
                <p className="text-gray-600">$120 / night</p>
              </div>
            </motion.div>
          ))}
        </div>
      </section>

      {/* CTA */}
      <section className="bg-gradient-to-r from-pink-500 to-red-500 text-white py-20 text-center">
        <motion.div
          initial={{ scale: 0.8, opacity: 0 }}
          whileInView={{ scale: 1, opacity: 1 }}
          transition={{ duration: 0.8 }}
        >
          <h2 className="text-4xl font-bold mb-4">
            Become a Host
          </h2>
          <p className="mb-6">Earn money by sharing your extra space</p>
          <button className="bg-white text-black px-6 py-3 rounded-full font-semibold shadow-lg">
            Get Started
          </button>
        </motion.div>
      </section>

      {/* FOOTER */}
      <footer className="bg-black text-white py-10 text-center">
        <p>© 2026 Airbnb Clone. All rights reserved.</p>
      </footer>
    </div>
  );
}
