#include<stdio.h>
#include<stdlib.h>
int a[20],n,front=-1,rear=-1;
void rear_enqueue()
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
void front_dequeue()
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
void front_enqueue()
{
if((front==rear+1) || (front==0 && rear==n-1))
printf("overflow\n");
else
{
if(front==-1)
front=rear=0;
else if(front==0)
front=n-1;
else
front=front-1;
scanf("%d",&a[front]);
}}
void rear_dequeue()
{
if(front==-1)
printf("underflow\n");
else
{
printf("%d\n",a[rear]);
if(front==rear)
front=rear=-1;
else if(rear==0)
rear=n-1;
else
rear=rear-1;
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
rear_enqueue();
else if(choice==2)
front_enqueue();
else if(choice==3)
front_dequeue();
else if(choice==4)
rear_dequeue();
else if(choice==5)
display();
else if(choice==6)
exit(0);
}
}
