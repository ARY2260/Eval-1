import { useRouter } from "next/router";

import { Header, Footer, QuestionDetailCard, Loading } from "../../components";

const Test = ({ test }) => {
  const router = useRouter();
  if (router.isFallback) {
    return <Loading />;
  }

  return (
    <>
      <Header />

      <div class="place-items-center py-12 px-20 bg-blue-200">
        <h2 class="mb-4 text-4xl font-extrabold"> 
          Test Details
        </h2>
        <div class="w-full max-w-lg">
        <div class="flex flex-wrap -mx-3 mb-6">
            <div class="w-full md:w-1/2 px-3">
              <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" for="grid-last-name">
                Title
              </label>
              <span class="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500">
                {test['test'].title}
              </span>
            </div>
          </div>
          <div class="flex flex-wrap -mx-3 mb-6">
            <div class="w-full px-3">
              <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" for="grid-password">
                Description
              </label>
              <span class="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-gray-500">
                {test['test'].description}
              </span>
              <p class="text-gray-600 text-sm italic">Created at: {test['test'].created_at}</p>
            </div>
          </div>
        </div>

        <div class="-mx-3 mb-6">
          <h3 class="mt-6 text-gray-600 text-2xl font-bold opacity-0.5 mb-2">
            Questions
          </h3>

          <div>
            {test['questions'].map((question) => (
              <QuestionDetailCard question={question} />
              // <QuestionDetailCard id={question.id} question={question.question_text} answer={question.expected_answer} max_score={question.max_score} />
            ))}
          </div>
        </div>
      </div>

      

      <Footer />  
    </>
  );
};

export async function getStaticPaths() {
  return {
    paths: [{params: {id: "1"}}],
    fallback: true,
  }
}

export async function getStaticProps({ params }) {
  const res = await fetch(`http://127.0.0.1:8000/api/tests/${params.id}/`);
  const test = await res.json();  
  return {
    props: {
      test,
    }
  };
}

export default Test;