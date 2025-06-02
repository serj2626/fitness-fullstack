import { SocialIcons } from "../icons/types/social-icons";

interface ISocialLinks {
  icon: string;
  link: string;
}

export const socials: ISocialLinks[] = [
  {
    icon: SocialIcons.GITHUB,
    link: "https://github.com/BS-Dev",
  },
  {
    icon: SocialIcons.LINKEDIN,
    link: "https://www.linkedin.com/in/bs-dev/",
  },
  {
    icon: SocialIcons.TELEGRAM,
    link: "https://t.me/bs_dev",
  },
  {
    icon: SocialIcons.WHATSAPP,
    link: "https://wa.me/79999999999",
  },
  {
    icon: SocialIcons.MAIL,
    link: "mailto:bs-dev@bk.ru",
  },
];
