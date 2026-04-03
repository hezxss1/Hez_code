import Head from 'next/head'

export default function Home() {
  return (
    <div className="min-h-screen bg-gray-900 text-white p-8">
      <Head>
        <title>Hez_code Dashboard</title>
      </Head>
      <main>
        <h1 className="text-4xl font-bold mb-8">Hez_code Dashboard</h1>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          <div className="bg-gray-800 p-6 rounded-lg">
            <h2 className="text-2xl font-semibold mb-4">Vanilla Visa Tools</h2>
            <ul className="space-y-2">
              <li><a href="/tools/vanilla_brute" className="text-blue-400 hover:underline">Brute-Forcer</a></li>
              <li><a href="/tools/vanilla_harvester" className="text-blue-400 hover:underline">Live Harvester</a></li>
            </ul>
          </div>
          <div className="bg-gray-800 p-6 rounded-lg">
            <h2 className="text-2xl font-semibold mb-4">Stripe Tools</h2>
            <ul className="space-y-2">
              <li><a href="/tools/stripe_sk_harvester" className="text-blue-400 hover:underline">SK Key Harvester</a></li>
            </ul>
          </div>
          <div className="bg-gray-800 p-6 rounded-lg">
            <h2 className="text-2xl font-semibold mb-4">Generate New Tool</h2>
            <form className="space-y-4">
              <input type="text" placeholder="Describe your tool..." className="w-full p-2 bg-gray-700 rounded" />
              <button type="submit" className="w-full bg-blue-600 hover:bg-blue-700 text-white p-2 rounded">Generate</button>
            </form>
          </div>
        </div>
      </main>
    </div>
  )
}