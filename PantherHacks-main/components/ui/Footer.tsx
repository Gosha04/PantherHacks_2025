import React from 'react';
import Link from 'next/link';
import Image from "next/image";

const Footer = () => {
  const githubRepoUrl = 'https://github.com/divinewton/PantherHacks';
  const devpostUrl = 'https://pantherhacks.devpost.com/';

  return (
    <footer className="flex flex-col gap-2 items-center justify-center w-full mt-auto">
      <div className="pt-10 text-center">
        <p className="text-sm text-muted-foreground">
          A PantherHacks 2025 Project
        </p>
      </div>
    <div className="p-0 flex flex-row gap-1">
      <div className="text-center">
      <Link
          href={githubRepoUrl}
          target="_blank"
          rel="noopener noreferrer"
          >
            <div className="p-1">
            <Image
            src="/github.png"
            width={25}
            height={25}
            alt="GitHub"
            className="opacity-75"
            />
        </div>
        </Link>
      </div>
      <div className="text-center">
      <Link
          href={devpostUrl}
          target="_blank"
          rel="noopener noreferrer"
          >
        <div className="p-1">
            <Image
            src="/devpost.svg"
            width={25}
            height={25}
            alt="DevPost"
            className="opacity-75"
            />
        </div>
        </Link>
      </div>
      </div>
    </footer>
  );
};

export default Footer;