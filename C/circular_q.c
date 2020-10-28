#include<stdio.h>
#include<stdlib.h>
int a[20],n,front=-1,rear=-1;
void enqueue()
{
if((front==rear+1) || (front==0 && rear==n-1))
printf("overflow\n");
else
{
if(front==-1)
front=0;
rear=(rear+1)%n;
scanf("%d",&a[rear]);
}}
void dequeue()
{
if(front==-1)
printf("underflow\n");
else
{
printf("%d\n",a[front]);
if(front==rear)
front=rear=-1;
else
front=(front+1)%n;
}}
void display()
{
if(front==-1)
printf("underflow\n");
else
{
for(int i=front;i!=rear;i=(i+1)%n)
printf("%d ",a[i]);
printf("%d",a[rear]);
printf("\n");
}}
int main()
{
int choice;
scanf("%d",&n);
while(1)
{
scanf("%d",&choice);
if(choice==1)
enqueue();
else if(choice==2)
dequeue();
else if(choice==3)
display();
else if(choice==4)
exit(0);
}}
