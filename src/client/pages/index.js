import Image from 'next/image'
import { Inter } from '@next/font/google'

import { Header, Footer } from '../components'
import { logo, examsheet, box, flask, django, cohere } from '../public'

const inter = Inter({ subsets: ['latin'] })

function Home({ tests }) {
  return (
    <>
      <Header />

      <div class="w-full overflow-hidden flex flex-row p-[112px_64px] box-border items-center justify-start gap-[80px] text-[56px]">
        <div class="flex-1 flex flex-col items-start justify-start gap-[24px]">
          <div class="self-stretch flex flex-col items-start justify-start gap-[24px]">
            <b class="self-stretch relative leading-[120%] inline-block">Grading Objective Questions with AI and Semantic Analysis</b>
            <div class="self-stretch relative text-lg leading-[150%] inline-block">
              Eval is an AI solution for grading objective questions. It uses
              advanced semantic analysis applied over the powerful Cohere-APIs to accurately
              evaluate student responses.
            </div>
          </div>
          <div class="flex flex-row p-[16px_0px_0px] box-border items-start justify-start gap-[16px]">
            {/* <button class="cursor-pointer [border:1px_solid_#000] p-[12px_24px] bg-[transparent] box-border flex flex-row items-center justify-center">
              <div class="relative text-base leading-[150%] font-roboto text-black text-left inline-block">
                Teacher
              </div>
            </button> */}
            <button class="cursor-pointer p-[10px_20px] bg-teal-700 flex flex-row items-center justify-center rounded">
              <div class="relative text-base leading-[150%] font-roboto text-white text-left inline-block">
                Get Started
              </div>
            </button>
          </div>
        </div>
        <Image
          class="flex-1 relative max-w-full overflow-hidden object-cover"
          alt=""
          src={examsheet}
        />
      </div>
      <div class="w-full overflow-hidden flex flex-col p-[112px_64px] box-border items-center justify-start gap-[80px] text-center">
        <b class="relative leading-[120%] inline-block w-[768px]">How it works [at a glance]</b>
        <div class="self-stretch flex flex-row items-start justify-center gap-[48px] text-xl">
          <div class="flex-1 flex flex-col items-center justify-start gap-[24px]">
            <Image
              class="relative w-[48px] h-[48px] shrink-0 overflow-hidden"
              alt=""
              src={box}
            />
            <div class="self-stretch flex flex-col items-start justify-start gap-[24px]">
              <b class="self-stretch relative leading-[140%] inline-block">Submit Questions with Answers</b>
              <div class="self-stretch relative text-base leading-[150%] inline-block">
                To get started with Eval, simply upload your set of objective
                questions and the corresponding correct answers.
              </div>
            </div>
          </div>
          <div class="flex-1 flex flex-col items-center justify-start gap-[24px]">
            <Image
              class="relative w-[48px] h-[48px] shrink-0 overflow-hidden"
              alt=""
              src={box}
            />
            <div class="self-stretch flex flex-col items-start justify-start gap-[24px]">
              <b class="self-stretch relative leading-[140%] inline-block">User Answers the Question</b>
              <div class="self-stretch relative text-base leading-[150%] inline-block" >
                Next, have your students or users answer the questions. They can
                do this through your platform or by manually entering their
                responses.
              </div>
            </div>
          </div>
          <div class="flex-1 flex flex-col items-center justify-start gap-[24px]">
            <Image
              class="relative w-[48px] h-[48px] shrink-0 overflow-hidden"
              alt=""
              src={box}
            />
            <div class="self-stretch flex flex-col items-start justify-start gap-[24px]">
              <b class="self-stretch relative leading-[140%] inline-block">Marking and Analysis of Answers</b>
              <div class="self-stretch relative text-base leading-[150%] inline-block">
                Once the answers have been submitted, Eval uses advanced
                semantic analysis, including cohere, to evaluate the quality of
                the responses. We then provide a detailed analysis of each
                answer and mark the questions accordingly.
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="w-full overflow-hidden flex flex-col p-[80px_64px] box-border items-center justify-start gap-[48px] text-lg">
        <b class="relative leading-[150%] inline-block">Built Using</b>
        <div class="self-stretch flex flex-col items-start justify-center">
          <div class="w-full flex flex-row justify-center items-center gap-[32px] ">
            <Image class="relative h-[83px] shrink-0 object-cover" alt="" src={flask} />
            <Image class="relative h-[55px] shrink-0 object-cover" alt="" src={django} />
            <Image class="relative h-[83px]  shrink-0 object-cover" alt="" src={cohere} />
          </div>
        </div>		  
      </div>

      <Footer />
    </>
  )
}

export default Home;