import Image from 'next/image';
import Link from 'next/link';

import { Header, Footer } from '../../components';
import { logo } from '../../public';

function Tests({ tests }) {
  return (
    <>
      <Header />

      <div class="place-items-center py-12 px-20 bg-blue-200">
        <h2 class="mb-4 text-4xl font-extrabold"> 
          Tests 
        </h2>
        {/* {console.log(tests)} */}
        {tests.map((test) => (
          <Link key={test.id} href={`/tests/${encodeURIComponent(test.id)}`}>
            <div class="flex items-center justify-between flex-wrap bg-white p-4 rounded-lg shadow-lg mb-3">
              <div class="">
                <h2 class="text-2xl font-bold mb-2 text-gray-800">{test.title}</h2>
                <p class="text-gray-700">{test.description}</p>
              </div>
              <span class="text-sm text-gray-700 italic">Created at: {test.created_at}</span>
            </div>
          </Link>
        ))}
      </div>

      <Footer />
    </>
  )
}

export async function getStaticProps() {
  const res = await fetch('http://127.0.0.1:8000/api/tests');
  const tests = await res.json();

  return {
    props: {
      tests
    }
  };
}

export default Tests;