import Image from "next/image";

import { flask, django, cohere } from "../public";

const Technologies = () => {
  return (
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
  );
};

export default Technologies;