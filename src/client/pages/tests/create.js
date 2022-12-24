import { useState } from 'react';

import { Header, Footer, QuestionFormCard } from '../../components';

const CreateTest = () => {
  const [components, setComponents] = useState(["Sample Component"]); 
  function addComponent() { 
    setComponents([...components, "Sample Component"]) 
  }

  return (
    <>
      <Header />

      <div class="place-items-center py-12 px-20">
        <h2 class="mb-6 text-4xl font-extrabold"> 
          Create new test
        </h2>
        <form class="w-full max-w-lg mb-6">
          <div class="flex flex-wrap -mx-3 mb-6">
            <div class="w-full md:w-1/2 px-3">
              <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" for="grid-last-name">
                Title
              </label>
              <input class="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" id="grid-last-name" type="text" placeholder="Test name" />
            </div>
          </div>
          <div class="flex flex-wrap -mx-3 mb-6">
            <div class="w-full px-3">
              <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" for="grid-password">
                Description
              </label>
              <input class="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" id="grid-password" type="text" placeholder="Test description" />
            </div>
          </div>
          
          <div>
            <div class="flex flex-wrap -mx-3 mb-6">
              <h3 class="mt-6 text-gray-600 text-2xl font-bold opacity-0.5">
                Questions
              </h3>
            </div>
            <QuestionFormCard />
            <QuestionFormCard />
            <QuestionFormCard />
            <button onClick={addComponent} class="bg-blue-400 hover:bg-blue-700 text-white font-bold py-1 px-2 border border-blue-400 rounded"> Add Question </button>
          </div>
        </form>
        <button class="bg-blue-400 hover:bg-blue-700 text-white font-bold py-2 px-4 border border-blue-400 rounded"> Submit </button>
      </div>

      <Footer />
    </>
  );
};

export default CreateTest;